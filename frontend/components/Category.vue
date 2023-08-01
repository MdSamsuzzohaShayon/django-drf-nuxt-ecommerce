<template>
    <div class="container mx-auto px-2 py-2">
        <h2 class="text-4xl mt-12">Shop by categories</h2>
        <div class="categories grid gap-x-4 grid-cols-4 mt-8">
            <!-- grid gap-4 grid-cols-3 grid-rows-3 -->
            <div class="category-item w-full relative" v-for="cat in categoryList">
                <NuxtLink v-bind:to="'/categories/' + cat.id">
                    <div class="cat-titles absolute bottom-1 left-1">
                        <h4 class="text-2xl font-normal">{{ cat.name }}</h4>
                        <p class="text-xs font-normal">Cat des</p>
                    </div>
                    <img v-bind:src="cat.image" alt="" class="h-80 object-center object-cover">
                </NuxtLink>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useCategoryStore from '../stores/CategoryStore';
// https://dev.to/rafaelmagalhaes/pinia-and-nuxt-3-4ij5
const categoryStore = useCategoryStore();
const { categoryList } = storeToRefs(categoryStore);
</script>