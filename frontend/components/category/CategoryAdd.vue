<template>
    <div class="container mx-auto px-2 bg-teal-100">
        <h1>Category add</h1>
        <form class="flex flex-col gap-4" v-on:submit.prevent="categoryAddHandler">
            <div class="input-group w-full">
                <label for="category-name" class="text-teal-900">Name</label>
                <input required="true" type="text" id="category-name"
                    class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                    v-model="categoryName">
            </div>
            <div class="input-group flex justify-between gap-4">
                <label for="category-file" class="text-teal-900">Category Image</label>
                <input required="true" type="file" id="category-file" ref="uploadFile"
                    class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                    v-on:change="uploadFileChangeHandler">
            </div>
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2" type="submit">Add</button>
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

const categoryName = ref<null | string>(null);
const uploadFile = ref(null);


const elementStore = useElementStore();
const categoryStore = useCategoryStore();

const { errorMessageList, successMessageList } = storeToRefs(elementStore);

const formData = new FormData();
const uploadFileChangeHandler=(e: Event)=>{
    const fileInput = e.target as HTMLInputElement;
    if(fileInput.files){
        formData.set('image', fileInput.files[0]);
    }
}


const categoryAddHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();
    if(categoryName.value && uploadFile.value){
        formData.set('name', categoryName.value);
        const token = useCookie('token');
        // @ts-ignore
        const {access: accessToken} = token.value;
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
            // Add a category to category list
            categoryStore.addNewCategory(data.value);
            const formElement = e.target as HTMLFormElement;
            formElement.reset();
        } else {
            elementStore.setErrorMessageList([JSON.stringify(error.value)]);
        }
    }
}
</script>

<style scoped></style>