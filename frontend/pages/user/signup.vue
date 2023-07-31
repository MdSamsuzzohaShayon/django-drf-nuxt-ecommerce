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
        <NuxtLink to="/user/signin">Already have an account? login.</NuxtLink>
        <br>
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

const { userSignup } = storeToRefs(userStore);
const { errorMessageList, successMessageList } = storeToRefs(elementStore);

const signupHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    const validData = userStore.serializedUserSignup
    if (validData) {
        // https://youtrack.jetbrains.com/issue/WEB-58600
        // @ts-ignore
        const { data, pending, error, refresh, status } = await useFetch(`${BACKEND_URL}/accounts/signup/`, {
            method: "POST",
            body: validData
        });
        console.log({ data: data.value, pending: pending.value, error: error.value, refresh: refresh, status: status.value });
        if (data.value) {
            if (status.value === 'success') {
                elementStore.setSuccessMessageList(Object.values(data.value));
            } else {
                elementStore.setErrorMessageList(Object.values(data.value))
            }
        }

    }
}

</script>

<style scoped></style>