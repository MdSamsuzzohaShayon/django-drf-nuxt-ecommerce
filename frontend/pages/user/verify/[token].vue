<template>
    <div>
        <NuxtLink to="/user/signin">Login</NuxtLink>

        <p class="text-red-900 px-4 py-2" v-for="message in errorMessageList">{{ message }}</p>
        <p class="text-teal-900 px-4 py-2" v-for="message in successMessageList">{{ message }}</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementStore from '../../../stores/ElementsStore';
const token = useRoute().params.token;

const elementStore = useElementStore();
const { errorMessageList, successMessageList } = storeToRefs(elementStore);

onMounted(async () => {
    console.log("onMounted");
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    if (token) {
        try {
            const response = await fetch(`${BACKEND_URL}/accounts/verify/${token}/`, {
                method: "PUT"
            });
            const responseObj = await response.json();
            if (response.status === 200) {
                elementStore.setSuccessMessageList(Object.values(responseObj))
            } else {
                elementStore.setErrorMessageList(Object.values(responseObj));
            }
            // console.log(Object.values(responseObj));
        } catch (error) {
            elementStore.setErrorMessageList([JSON.stringify(error)])
        }

    }
});
</script>

<style lang="scss" scoped></style>