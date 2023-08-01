<template>
    <div class="container mx-auto px-2 bg-teal-100">
        <h1>Login</h1>
        <UserSignin v-bind:is_staff="false" />
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '../../stores/UserStore';


const userStore = useUserStore();

const { isAuthenticated } = storeToRefs(userStore);

onMounted(()=>{
    if(isAuthenticated.value === true){
        navigateTo('/user/dashboard/');
    }
});
</script>

<style scoped></style>