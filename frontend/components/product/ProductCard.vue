<template>
    <div class="card text-center">
        <img v-bind:src="product.image1" class="h-60" alt="">
        <p class="font-bold text-gray-500 m-4 truncate">{{ product.title }}</p>
        <NuxtLink v-bind:to="`/products/${product.id}/`">
        <p class="btn my-4">View Details</p></NuxtLink>
    </div>
</template>

<script setup>
const { product } = defineProps(['product'])

</script>

<style scoped></style>