<template>
    <div>
        <ProductDetail v-bind:product="product" />
    </div>
</template>

<script setup>
const { id } = useRoute().params;
const uri = "http://localhost:8000/api/products/" + id + "/";
const {data: product} = await useFetch(uri, {key: id});

if (!product.value){
    throw createError({statusCode: 404, statusMessage: "Product not found", fetal: true});
}

definePageMeta({
    layout: 'products'
});

</script>

<style scoped></style>