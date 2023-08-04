<template>
    <div class="container mx-auto px-2">
        <h1>Cart</h1>
        <div class="cart-list">
            <div class="cart" v-for="c in cartList" v-bind:key="c.id">
                <div v-if="findProductById(c.pId)" v-bind:set="product = findProductById(c.pId)"
                    class="flex justify-between items-center bg-teal-100 mb-2">
                    <img v-bind:src="findProductById(c.pId)?.image1" alt="" class="w-44">
                    <h3>{{ product?.title }}</h3>
                    <div class="seg-1 flex flex-col justify-center items-center h-full">
                        <p class="w-fit">Total Price - ৳{{ product.discount_price ? product.discount_price * c.qty :
                            product.price * c.qty }}</p>
                        <div class="q-controller flex items-center justify-center">
                            <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="qtyChange(true)">
                                <Icon name="ep:plus" size="20" color="blue" />
                            </button>
                            <p>Quantity: {{ c.qty }}</p>
                            <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="qtyChange(false)">
                                <Icon name="ep:minus" size="20" color="blue" />
                            </button>
                        </div>
                    </div>
                    <div class="seg-2 flex flex-col px-2 gap-2">
                        <NuxtLink v-bind:to="`/checkout/${c.id}/`">
                            <button class="p-2 bg-teal-900 text-teal-100 w-full">Checkout</button>
                        </NuxtLink>
                        <button type="button" v-on:click.prevent="removeFromCart(c.id)"
                            class="bg-red-800 text-red-100 p-2 w-full">
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useProductStore from '../../stores/ProductStore';
import { ProductInterface } from '../../types/ProductType';

const productStore = useProductStore();

await productStore.fetchProducts();
productStore.fetchCartFromLocalStorage();

const { cartList, productList } = storeToRefs(productStore);

const findProductById = (pId: number) => {
    const findProduct: ProductInterface | undefined = productList.value.find((p: ProductInterface) => p.id === pId);
    if (findProduct) return findProduct;
    return null;
}

const qtyChange = (addQty: boolean) => {
    if (addQty) {
        console.log("Add more");
    } else {
        console.log("Sub more");
    }
}


const removeFromCart = (cId: string) => {
    productStore.removeItemFromCart(cId);
}
</script>

<style lang="scss" scoped></style>