<template>
    <div>
        <h1>Order List</h1>
        <!-- orderList -->
        <table class="w-full ">
            <thead>
                <tr>
                    <th class="p-2 text-center border border-teal-900">ID</th>
                    <th class="p-2 text-center border border-teal-900">Product</th>
                    <th class="p-2 text-center border border-teal-900">Status</th>
                    <th class="p-2 text-center border border-teal-900">Quantity</th>
                    <th class="p-2 text-center border border-teal-900">Address</th>
                    <th class="p-2 text-center border border-teal-900">Total Price (৳)</th>
                    <th class="p-2 text-center border border-teal-900">Perform</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="order in organizedOrders()">
                    <td class="p-2 text-center border border-teal-900/50">{{ order.id }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ order.product }}</td>
                    <td class="p-2 text-center border border-teal-900/50 capitalize">{{ order.status }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ order.quantity }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ order.address }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ order.total }}</td>
                    <td class="p-2 text-center border border-teal-900/50 flex flex-col">
                        <p class="cursor-pointer text-red-900" v-on:click.prevent="deleteOrderHandler(order.id)">Cancel</p>
                        <NuxtLink v-bind:to="`/orders/${order.id}/`">
                            <p class="cursor-pointer text-teal-900">View</p>
                            <!-- <Icon class="pr-2" size="20" name="bytesize:eye" color="teal" /> -->
                        </NuxtLink>
                        <p v-if="userInfo.is_staff" class="cursor-pointer text-teal-900" v-on:click.prevent="updateOrderHandler(order.id)">Update</p>
                        <!-- <Icon v-if="userInfo.is_staff" class="pr-2" size="20" name="line-md:edit" v-on:click.prevent="updateOrderHandler(order.id)"
                            color="teal" /> -->
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useOrderStore from '../../stores/OrderStore';
import useProductStore from '../../stores/ProductStore';
import useUserStore from '../../stores/UserStore';
import { OrderStatus, OrganizedOrderInterface } from '../../types/ProductOrderType';

const ordersStore = useOrderStore();
const productStore = useProductStore();
const userStore = useUserStore();

const { orderList } = storeToRefs(ordersStore);
const { userInfo } = storeToRefs(userStore);

const deleteOrderHandler = (pId: number | null) => {
    console.log("Delete order -> ", pId);
}

const updateOrderHandler = (pId: number) => {
    // ordersStore.setOrderUpdate(true);
    // ordersStore.setOrderToUpdate(pId);
}



const organizedOrders = () => {
    const newOrderList: OrganizedOrderInterface[] = [];
    const ol = orderList.value;
    for (let i = 0; i < ol.length; i++) {
        // product: number;
        // address: number;
        let status = "PENDING";
        if (ol[i].status === OrderStatus.COMPLETED) {
            status = "COMPLETED";
        } else if (ol[i].status === OrderStatus.SHIPPING) {
            status = "SHIPPING";
        }

        const findProduct = productStore.productList.find(p => p.id === ol[i].product);
        // console.log(userInfo.value.address[i]);

        const newOrder: OrganizedOrderInterface = {
            id: ol[i].id,
            status: status,
            is_paid: ol[i].is_paid,
            product: findProduct ? findProduct.title : '',
            quantity: ol[i].quantity,
            address: `${userInfo.value.address[0]?.area}, ${userInfo.value.address[0]?.city}`,
            total: ol[i].total,
        }
        newOrderList.push(newOrder);
    }
    return newOrderList;
}

</script>

<style scoped></style>