<template>
    <div class="container mx-auto px-2 bg-teal-100">
        <h1>Login</h1>
        <form class="flex flex-col gap-4" v-on:submit.prevent="signinHandler">
            <div class="input-group w-full">
                <label for="user-email" class="text-teal-900">Email</label>
                <input required="true" type="email" id="user-email"
                    class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                    v-model="userSignin.email">
            </div>
            <div class="input-group flex justify-between gap-4">
                <label for="user-password" class="text-teal-900">Password</label>
                <input required="true" type="password" id="user-password"
                    class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                    v-model="userSignin.password">
            </div>
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2" type="submit">Login</button>
            </div>
        </form>
        <NuxtLink to="/user/passwordforget">Password forgotten?</NuxtLink>
        <NuxtLink to="/user/signup">Don't have an account? register.</NuxtLink>
        <p class="text-red-900 px-4 py-2 capitalize" v-for="message in errorMessageList">{{ message }}</p>
        <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }}</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '../../stores/UserStore';
import useElementStore from '../../stores/ElementsStore';

const userStore = useUserStore();
const elementStore = useElementStore();

const { userSignin } = storeToRefs(userStore);
const { errorMessageList, successMessageList } = storeToRefs(elementStore);


const signinHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    const validData = userStore.serializedUserSignin
    if (validData) {
        // https://youtrack.jetbrains.com/issue/WEB-58600
        const { data, pending, error, refresh, status } = await useFetch(`${BACKEND_URL}/accounts/signin/`, {
            method: "POST",
            body: validData
        });
        console.log({ data: data.value, pending: pending.value, error: error.value, refresh: refresh, status: status.value });
        if (data.value) {
            if (status.value === 'success') {
                window.localStorage.setItem("token", JSON.stringify(data.value));
                await navigateTo("/user/dashboard/");
            } else {
                elementStore.setErrorMessageList(Object.values(data.value));
            }
        }
        if (error.value) {
            if (error.value.statusCode == 401) {
                elementStore.setErrorMessageList(["Invalid credentials!"]);
            } else {
                elementStore.setErrorMessageList([JSON.stringify(error.value)]);
            }
        }
    } else {
        elementStore.setErrorMessageList(["Invalid data!"]);
    }
}
</script>

<style scoped></style>