<template>
    <div class="container mx-auto px-2">
        <h1>Checkout</h1>
        <h2>Check if payment is completed or not. </h2>
        <p>Pay via bkash</p>
        <p>If payment is completed delete this from cart</p>
        <p>And add a order in order section</p>
        <p class="bg-teal-200">Select shipping address</p>
        <div class="shipping" v-if="userInfo.address.length > 0">
            <p>Phone: {{ userInfo.address[0].phone }}</p>
            <p>Area: {{ userInfo.address[0].area }}</p>
            <p>City: {{ userInfo.address[0].city }}</p>
            <button type="button" class="bg-teal-900 text-teal-100 p-2" v-on:click="addAddressHandler">Edit</button>
        </div>
        <br>
        <button class="p-2 bg-teal-900 text-teal-100 mr-2" v-on:click="payAndOrderHandler">Cash on delivery</button>
        <button class="p-2 bg-teal-900 text-teal-100" v-on:click="payAndOrderHandler">Pay via BKash</button>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useProductStore from '../../stores/ProductStore';
import useElementsStore from '../../stores/ElementsStore';
import useUserStore from '../../stores/UserStore';
import userOrderStore from '../../stores/OrderStore';
import { OrderInterface } from '../../types/ProductOrderType';

const productStore = useProductStore();
const elementsStore = useElementsStore();
const userStore = useUserStore();
const orderStore = userOrderStore();

productStore.fetchCartFromLocalStorage();

const { cId } = useRoute().params;

const { userInfo } = storeToRefs(userStore);
// console.log(cId);

const addAddressHandler = (e: Event) => {

}

const payAndOrderHandler = async (e: Event) => {
    e.preventDefault();

    // Redirect to order page
    const token = useCookie('token');
    // @ts-ignore
    const { access: accessToken } = token.value;
    const cart = productStore.getCartById(cId);
    if (!cart) return elementsStore.setErrorMessageList(["Product not found!"]);
    const { data: orderData, status: orderStatus } = await useFetch<OrderInterface>(`${BACKEND_URL}/orders/new/`, {
        key: cId,
        method: "POST",
        body: {
            product: cart.pId,
            quantity: cart.qty,
            address: userInfo.value.address[0].id,
        },
        headers: {
            "Authorization": `Bearer ${accessToken}`
        }
    });
    if (orderStatus.value === 'success' && orderData.value) {
        orderStore.addNewOrder(orderData.value);
        navigateTo("/user/dashboard/");
    } else {
        elementsStore.setErrorMessageList(["Invalid cart item!"]);
    }

}

</script>

<style scoped></style>