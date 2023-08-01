<template>
    <div>
        <div class="grid grid-cols-4 gap-5">
            <div v-for="p in productList">
                <!-- <NuxtLink v-bind:to="`/products/${p.id}/`">{{ p.title }}</NuxtLink> -->
                <ProductCard v-bind:product="p" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import useProductStore from '../../stores/ProductStore';
import { storeToRefs } from 'pinia';
const { catId } = useRoute().params;

const productStore = useProductStore();
const { productList } = storeToRefs(productStore);
// const { data: products } = await useFetch('http://localhost:8000/api/products/');
// const { data: products } = await useFetch<ProductInterface[]>(`${BACKEND_URL}/products/categories/${catId}`);

await productStore.fetchProductsByCategory(catId)
</script>

<style lang="scss" scoped></style>