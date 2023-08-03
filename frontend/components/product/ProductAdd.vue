<template>
    <div class="container mx-auto px-2 bg-teal-100">
        <h1>Product add {{ productUpdate }}</h1>
        <form class="flex flex-col gap-4" v-on:submit.prevent="productAddHandler">
            <div class="input-group w-full">
                <label for="product-title" class="text-teal-900">Title</label>
                <input v-bind:required="productUpdate === false ? true : false" type="text" id="product-title"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-model="productUpdateAdd.title">
            </div>
            <div class="input-group w-full">
                <label for="product-price" class="text-teal-900">Price</label>
                <input v-bind:required="productUpdate === false ? true : false" type="number" id="product-price"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-model="productUpdateAdd.price">
            </div>
            <div class="input-group w-full">
                <label for="product-discount" class="text-teal-900">Discount Price</label>
                <input type="number" id="product-discount"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-model="productUpdateAdd.discount_price">
            </div>
            <div class="input-group w-full">
                <label for="product-total-stock" class="text-teal-900">Total Stock</label>
                <input v-bind:required="productUpdate === false ? true : false" type="number" id="product-total-stock"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-model="productUpdateAdd.total_stock">
            </div>
            <div class="input-group w-full">
                <label for="product-total-stock" class="text-teal-900">Description</label>
                <textarea id="product-total-stock" rows="3"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-model="productUpdateAdd.description"></textarea>
            </div>
            <div class="input-group w-full">
                <label for="product-category" class="text-teal-900">Category</label>
                <select id="product-category" v-model="productUpdateAdd.category"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2">
                    <option v-for="category in categoryList" v-bind:value="category.id">{{ category.name }}</option>
                </select>
            </div>

            <!-- Images  -->
            <div class="input-group flex justify-between gap-4">
                <label for="product-image-1" class="text-teal-900">Product Image 1</label>
                <input v-bind:required="productUpdate === false ? true : false" type="file" name="image1"
                    id="product-image-1" ref="uploadImage1"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-on:change="uploadFileChangeHandler">
            </div>
            <div class="input-group flex justify-between gap-4">
                <label for="product-image-2" class="text-teal-900">Product Image 2</label>
                <input type="file" name="image2" id="product-image-2" ref="uploadImage2"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-on:change="uploadFileChangeHandler">
            </div>
            <div class="input-group flex justify-between gap-4">
                <label for="product-image-3" class="text-teal-900">Product Image 3</label>
                <input type="file" name="image3" id="product-image-3" ref="uploadImage3"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-on:change="uploadFileChangeHandler">
            </div>
            <div class="input-group flex justify-between gap-4">
                <label for="product-image-4" class="text-teal-900">Product Image 4</label>
                <input type="file" name="image4" id="product-image-4" ref="uploadImage4"
                    class="bg-real-100 text-teal-950 outline-0 text-base border border-teal-950 w-full p-2"
                    v-on:change="uploadFileChangeHandler">
            </div>
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2" type="submit">{{ productUpdate ?
                    'Update' : 'Add' }}</button>
            </div>
        </form>
        <p class="text-red-900 px-4 py-2 capitalize" v-for="message in errorMessageList">{{ message }}</p>
        <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }}</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementStore from '../../stores/ElementsStore';
import useProductStore from '../../stores/ProductStore';
import useCategoryStore from '../../stores/CategoryStore';
import { ProductInterface } from '../../types/ProductType';
import { BACKEND_URL } from '../../utils/keys';

const uploadImage1 = ref(null);
const uploadImage2 = ref(null);
const uploadImage3 = ref(null);
const uploadImage4 = ref(null);

const elementStore = useElementStore();
const productStore = useProductStore();
const categoryStore = useCategoryStore();

const { errorMessageList, successMessageList } = storeToRefs(elementStore);
const { productUpdateAdd, productUpdate } = storeToRefs(productStore);
const { categoryList } = storeToRefs(categoryStore);

// Form data
const formData = new FormData();

const uploadFileChangeHandler = (e: Event) => {
    const fileInput = e.target as HTMLInputElement;
    if (fileInput.files) {
        formData.set(fileInput.name, fileInput.files[0]);
    }
}


const productAddHandler = async (e: Event) => {
    elementStore.resetErrorMessageList();
    elementStore.resetSuccessMessageList();

    const newObj: any = { ...productUpdateAdd.value };
    if (newObj.image1) delete newObj.image1;
    if (newObj.image2) delete newObj.image2;
    if (newObj.image3) delete newObj.image3;
    if (newObj.image4) delete newObj.image4;

    for (const [k, v] of Object.entries(newObj)) {
        // @ts-ignore
        formData.set(k, v);
    }
    // @ts-ignore
    for (const pair of formData.entries()) {
        console.log(`${pair[0]}, ${pair[1]}`);
    }

    const token = useCookie('token');
    // @ts-ignore
    const { access: accessToken } = token.value;
    // /products/1/update/ 
    let url = `${BACKEND_URL}/products/new/`;
    let method: "POST" | "PUT" = "POST"
    if (productUpdate.value === true) {
        url = `${BACKEND_URL}/products/${productUpdateAdd.value.id}/update/`;
        method = 'PUT';
    }
    const { data, pending, error, refresh, status } = await useFetch<ProductInterface>(url, {
        method: method,
        body: formData,
        headers: {
            "Authorization": `Bearer ${accessToken}`
        }
    });
    console.log({ data: data.value, pending: pending.value, error: error.value, refresh: refresh, status: status.value });
    if (status.value === 'success' && data.value) {
        // Add a product to product list
        if (productUpdate.value === true) {
            productStore.setUpdateProduct(productUpdateAdd.value.id);
        } else {
            productStore.addNewProduct(data.value);
        }
        const formElement = e.target as HTMLFormElement;
        formElement.reset();
    } else {
        elementStore.setErrorMessageList([JSON.stringify(error.value)]);
    }
}
</script>

<style scoped></style>