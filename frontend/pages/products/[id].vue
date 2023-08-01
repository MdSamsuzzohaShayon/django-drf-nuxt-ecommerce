<template>
    <div>
        <Head>
            <Title>Shakil Furniture | {{ product.title }}</Title>
            <Meta name="description" :content="product.description" />
        </Head>
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

