<template>
    <div>
        <div class="item mt-4 w-full bg-white" v-for="a in userInfo.address">
            <div class="p-4 flex justify-between items-center">
                <div class="text-detail">
                    <p>Area: {{ a.area }}</p>
                    <p>City: {{ a.city }}</p>
                    <p>Country: {{ a.country }}</p>
                    <p>Phone: {{ a.phone }}</p>
                </div>
                <div class="contaoller">
                    <p class="cursor-pointer text-teal-900">Update</p>
                    <p class="cursor-pointer text-red-900">Delete</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const { userInfo } = defineProps(['userInfo']);

</script>

<style scoped></style>