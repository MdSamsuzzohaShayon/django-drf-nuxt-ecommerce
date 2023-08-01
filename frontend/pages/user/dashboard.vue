<template>
    <div>
        <p>Product list</p>
        <p>Category list</p>
        <p>Settings</p>
        <p>Orders</p>
        <p>Users</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useUserStore from '../../stores/UserStore';

const userStore = useUserStore();

const { isAuthenticated } = storeToRefs(userStore);
onMounted(() => {
    if (!isAuthenticated) {
        navigateTo('/user/signin/');
    }
});
</script>

<style lang="scss" scoped></style>