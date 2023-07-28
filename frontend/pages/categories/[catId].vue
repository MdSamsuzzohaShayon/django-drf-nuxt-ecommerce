<template>
    <div>
        <div class="grid grid-cols-4 gap-5">
            <div v-for="p in products">
                <!-- <NuxtLink v-bind:to="`/products/${p.id}/`">{{ p.title }}</NuxtLink> -->
                <ProductCard v-bind:product="p" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ProductInterface } from '../../types/ProductType';
// const { data: products } = await useFetch('http://localhost:8000/api/products/');
const { data: products } = await useFetch<ProductInterface[]>(`${BACKEND_URL}/products/`);
</script>

<style lang="scss" scoped></style>