<template>
    <div>
        <h2>Product detail {{ id }}</h2>
        <p>{{ product.title }}</p>
        <p>{{ product.price }}</p>
        <p>{{ product.id }}</p>
    </div>
</template>

<script setup>
const { id } = useRoute().params;
const uri = "http://localhost:8000/api/products/" + id + "/";
const {data: product} = await useFetch(uri, {key: id});

definePageMeta({
    layout: 'products'
});

</script>

<style scoped></style>