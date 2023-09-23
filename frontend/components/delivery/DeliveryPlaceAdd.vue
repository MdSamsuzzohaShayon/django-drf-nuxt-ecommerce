<template>
    <div>
        <form class="flex flex-col gap-4 mt-4" v-on:submit.prevent="deliveryPlaceAddHandler">
            <div class="input-group w-full">
                <input v-bind:required="deliveryPlaceUpdate === false ? true : false" type="text" id="deliveryPlace-name"
                    class="bg-white text-teal-950 outline-0 px-3 py-2 border border-teal-950/25 w-full px-1 placeholder:text-teal-950/50"
                    placeholder="Name" v-model="deliveryPlaceName">
            </div>
            <div class="input-group w-full">
                <label for="deliveryPlace-image"
                    class="w-full bg-white text-teal-950/50  px-3 py-2 border border-teal-950/25 block"> <span>
                        <Icon name="ph:image" size="20" />
                    </span> {{ state.imageName !== '' ? state.imageName : 'Image' }}</label>
                <input v-bind:required="deliveryPlaceUpdate === false ? true : false" type="file" id="deliveryPlace-image"
                    name="image" ref="uploadFile" class="hidden" v-on:input="uploadFileChangeHandler">
            </div>
            <!-- Submit  -->
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2 w-full font-bold" type="submit">
                    {{ deliveryPlaceUpdate ? 'Update' : 'Add' }}</button>
            </div>
        </form>
        <p class="text-red-900 px-4 py-2 capitalize" v-for="message in errorMessageList">{{ message }}</p>
        <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }}</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementStore from '../../stores/ElementsStore';
import useCategoryStore from '../../stores/CategoryStore';
import { ProductCategoryInterface } from "../../types/ProductCategoryType";

const deliveryPlaceName = ref<null | string>(null);
const uploadFile = ref(null);
const state = reactive({
    imageName: '',
});

const deliveryPlaceUpdate = false;

const elementStore = useElementStore();
const deliveryPlaceStore = useCategoryStore();

const { errorMessageList, successMessageList } = storeToRefs(elementStore);

const formData = new FormData();
const uploadFileChangeHandler = (e: Event) => {
    const fileInput = e.target as HTMLInputElement;
    // @ts-ignore
    state[`${fileInput.name}Name`] = fileInput.files[0].name;
    if (fileInput.files) {
        formData.set('deliveryPlaceimage', fileInput.files[0]);
    }
}


const deliveryPlaceAddHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    if (deliveryPlaceName.value && uploadFile.value) {
        formData.set('name', deliveryPlaceName.value);
        const token = useCookie('token');
        // @ts-ignore
        const { access: accessToken } = token.value;
        const { data, pending, error, refresh, status } = await useFetch<ProductCategoryInterface>(`${BACKEND_URL}/products/categories/new/`, {
            method: "POST",
            body: formData,
            headers: {
                "Authorization": `Bearer ${accessToken}`
            }
        });
        console.log({ data: data.value, pending: pending.value, error: error.value, refresh: refresh, status: status.value });
        if (status.value === 'success' && data.value) {
            console.log(data.value);
            // Add a deliveryPlace to deliveryPlace list
            deliveryPlaceStore.addNewCategory(data.value);
            const formElement = e.target as HTMLFormElement;
            formElement.reset();
        } else {
            elementStore.setErrorMessageList([JSON.stringify(error.value)]);
        }
    }
}
</script>

<style scoped></style>