<template>
    <div class="card">
        <div class="grid grid-cols-2 gap-10">
            <div class="p-7">
                <img :src="product.image1" alt="" class="mx-auto my-7">
            </div>
            <div class="p-7">
                <h2 class="text-4xl my-7">{{ product.title }}</h2>
                <p class="text-xl my-7 line-through" v-if="product.discount_price && product.discount_price > 0" >Price - ৳{{ product.price }}</p>
                <p class="text-xl my-7" v-else>Price - ৳{{ product.price }}</p>
                <p class="text-xl my-7" v-if="product.discount_price && product.discount_price > 0">Current Price - ৳{{ product.discount_price }}</p>

                <h3 class="font-blod border-b-2 mb-4 pb-2">Product Description</h3>
                <p class="mb-7">{{ product.description }}</p>
                <div class="quantity">
                    <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="state.quantity++">
                        <Icon name="ep:plus" size="20" color="blue" />
                    </button>
                    <input type="number" v-bind:max="product.total_stock"
                        class="remove-arrow bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 p-2"
                        v-model="state.quantity" min="1">
                    <button class="bg-none text-teal-50 border-0 px-5 py-2" v-on:click.prevent="state.quantity--">
                        <Icon name="ep:minus" size="20" color="blue" />
                    </button>
                </div>
                <button class="btn flex" v-on:click="addToCartHandler">
                    <i class="material-icons mr-2">add_shopping_cart</i>
                    <span>Add to cart</span>
                </button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import useProductStore from '../../stores/ProductStore';
const { product } = defineProps(['product']);

const productStore = useProductStore();

const state = reactive({
    quantity: 1
});
// const { cartList } = storeToRefs(productStore)

const addToCartHandler = (e: Event) => {
    e.preventDefault();
    const newProduct = { id: `${window.crypto.randomUUID()}`, pId: product.id, qty: state.quantity };
    productStore.addItemToCart(newProduct);
}

</script>

<style scoped></style>