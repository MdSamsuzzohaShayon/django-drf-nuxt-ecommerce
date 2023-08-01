<template>
    <div>
        <h1>{{ productList.length }} items found</h1>
        <button class="filter-bar-control bg-teal-900 text-teal-50 flex" v-on:click.prevent="elementStore.openFilterBar()">
            Filter 
            <Icon name="clarity:filter-line" size="30" />
        </button>
        <ProductFilter />
        <div v-for="p in productList">
            <!-- <NuxtLink v-bind:to="`/products/${p.id}/`">{{ p.title }}</NuxtLink> -->
            <ProductCard v-bind:product="p" />
        </div>
    </div>
</template>

<script setup lang="ts">

import { storeToRefs } from 'pinia';
import useProductStore from '../stores/ProductStore';
import useElementStore from '../stores/ElementsStore';

const elementStore = useElementStore();
const productStore = useProductStore();
const { productList } = storeToRefs(productStore);

const params = new URLSearchParams(window.location.search);
await productStore.fetchProducts(params.get('q'));
</script>
