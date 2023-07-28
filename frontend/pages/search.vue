<template>
    <div>
        <h1>{{ productList.length }} items found</h1>
        <div v-for="p in productList">
            <!-- <NuxtLink v-bind:to="`/products/${p.id}/`">{{ p.title }}</NuxtLink> -->
            <ProductCard v-bind:product="p" />
        </div>
    </div>
</template>

<script setup lang="ts">

import { storeToRefs } from 'pinia';
import useProductStore from '../stores/ProductStore';

const productStore = useProductStore();
const { productList } = storeToRefs(productStore);

const params = new URLSearchParams(window.location.search);
await productStore.fetchProducts(params.get('q'));
</script>
