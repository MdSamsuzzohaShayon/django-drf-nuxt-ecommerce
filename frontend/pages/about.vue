<template>
    <div>
        <h2>About</h2>
        <p>{{ data }}</p>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolorum culpa cupiditate fugit nisi alias officiis eaque aliquid, minus architecto consectetur.</p>
    </div>
</template>

<script setup>
const {data} = await useFetch("/api/products/?name=anything", {
    method: 'POST',
    body: {age: 27}
});

useHead({
    title: 'Shakil Furniture | about',
    meta: [
        {name: 'description', content: 'A furniture website about page!'}
    ]
});

</script>

<style scoped>

</style>