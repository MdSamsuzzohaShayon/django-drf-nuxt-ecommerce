<template>
    <div class="container mx-auto px-2 bg-teal-100">
        <h1>Register</h1>
        <form class="flex flex-col gap-4" v-on:submit.prevent="signupHandler">
            <div class="input-group flex justify-between gap-4">
                <div class="input-sub-group w-1/2">
                    <label for="user-first-name" class="text-teal-900">First Name</label>
                    <input required="true" type="text" id="user-first-name"
                        class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                        v-model="userSignup.first_name">
                </div>
                <div class="input-sub-group w-1/2">
                    <label for="user-last-name" class="text-teal-900">Last Name</label>
                    <input required="true" type="text" id="user-last-name"
                        class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                        v-model="userSignup.last_name">
                </div>
            </div>
            <div class="input-group w-full">
                <label for="user-email" class="text-teal-900">Email</label>
                <input required="true" type="email" id="user-email"
                    class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                    v-model="userSignup.email">
            </div>
            <div class="input-group flex justify-between gap-4">
                <div class="input-sub-group w-1/2">
                    <label for="user-password" class="text-teal-900">Password</label>
                    <input required="true" type="password" id="user-password"
                        class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                        v-model="userSignup.password">
                </div>
                <div class="input-sub-group w-1/2">
                    <label for="user-confirm-password" class="text-teal-900">Confirm Password</label>
                    <input required="true" type="password" id="user-confirm-password"
                        class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                        v-model="userSignup.confirm_password">
                </div>
            </div>
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2" type="submit">Register</button>
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '../../stores/UserStore';

const userStore = useUserStore();
const { userSignup } = storeToRefs(userStore);

const signupHandler = async (e: Event) => {
    const validData = userStore.serializedUserSignup
    console.log(validData);
    if (validData) {
        // https://youtrack.jetbrains.com/issue/WEB-58600
        // @ts-ignore
        const { data, pending, error, refresh } = await useFetch(`${BACKEND_URL}/accounts/signup/`, validData);
        console.log({ data, pending, error, refresh });
    }
}

</script>

<style scoped></style>