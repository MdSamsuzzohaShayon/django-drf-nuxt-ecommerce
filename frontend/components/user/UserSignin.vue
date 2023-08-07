<template>
    <div class="container mx-auto px-2 ">
        <div class="message-content w-full mt-8">
            <p class="text-red-900 px-4 py-2 capitalize w-full bg-red-100 text-red-900" v-for="message in errorMessageList">
                {{ message }} <span class="float-right">
                    <Icon name="grommet-icons:close" size="20" v-on:click.prevent="elementStore.resetErrorMessageList()" />
                </span> </p>
            <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }} <span
                    class="float-right">
                    <Icon name="grommet-icons:close" size="20"
                        v-on:click.prevent="elementStore.resetSuccessMessageList()" />
                </span> </p>
        </div>
        <div class="main-content flex flex-col md:flex-row justify-start gap-8">
            <div class="sign-in w-full md:w-2/5">
                <h1 class="pt-8">Login</h1>
                <form class="flex flex-col gap-4 mt-8" v-on:submit.prevent="signinHandler">
                    <div class="input-group w-full">
                        <input required="true" type="email" id="user-email"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Email" v-model="userSignin.email">
                    </div>
                    <div class="input-group flex justify-between gap-4">
                        <input required="true" type="password" id="user-password"
                            class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                            placeholder="Password" v-model="userSignin.password">
                    </div>
                    <div class="input-group w-full">
                        <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold"
                            type="submit">Login</button>
                    </div>
                    <div class="input-group w-full flex flex-col">
                        <NuxtLink to="/user/passwordforget" class="underline">Password forgotten?</NuxtLink>
                        <NuxtLink to="/user/signup" class="underline">Don't have an account? register.</NuxtLink>
                    </div>
                </form>
            </div>

            <div class="new-customer w-full md:w-2/5">
                <h1 class="pt-8">New Customer</h1>
                <p class="mt-8 mb-2">Sign up for early Sale access plus tailored new arrivals,trends and promotions. To opt
                    out,
                    click unsubscribe in our emails.</p>
                <NuxtLink to="/user/signup">
                    <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 font-bold"
                        type="button">Register</button>
                </NuxtLink>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '../../stores/UserStore';
import useElementStore from '../../stores/ElementsStore';
import { UserTokenInterface } from '../../types/UserType'

const oneDayInSeconds = 24 * 60 * 60; // 1 day = 24 hours * 60 minutes * 60 seconds

const props = defineProps({
    is_staff: Boolean
});


const userStore = useUserStore();
const elementStore = useElementStore();

const { userSignin, isAuthenticated } = storeToRefs(userStore);
const { errorMessageList, successMessageList } = storeToRefs(elementStore);


const signinHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    const validData = userStore.serializedUserSignin
    if (validData) {
        // https://youtrack.jetbrains.com/issue/WEB-58600
        const { data, pending, error, refresh, status } = await useFetch<UserTokenInterface>(`${BACKEND_URL}/accounts/signin/`, {
            method: "POST",
            body: validData
        });
        if (status.value === 'success' && data.value) {
            userStore.setIsAuthenticated(true);
            const token = useCookie("token", {
                maxAge: MAX_SIGNIN_COOKIE_AGE,
                // httpOnly: true, // On https protocal, Need to set by server 
            });
            token.value = JSON.stringify(data.value);

            // Fetch user with token we got
            if (data.value.access) await userStore.fetchUser(data.value.access);

            // document.cookie
            if (props.is_staff === true) {
                await navigateTo("/admin/");
            } else {
                await navigateTo("/user/dashboard/");
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