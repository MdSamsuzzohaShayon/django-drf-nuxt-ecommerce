<template>
    <div class="absolute top-0 left-0 w-60 bg-teal-100 h-screen px-6 pt-10 " v-if="showFilter">
        Product filter
        <button class="bg-none p-0 m-0">
            <Icon name="grommet-icons:close" size="20" class="text-teal-950"
                v-on:click.prevent="elementsStore.closeFilterBar()" />
        </button>
        <form class="flex flex-col gap-4" v-on:submit.prevent="applyFilterHandler">
            <div class="input-group w-full">
                <label for="product-title" class="text-teal-900">Title</label>
                <input type="text" id="product-title"
                    class="bg-real-100 text-teal-950 outline-0 text-3xl border border-teal-950 w-full px-1"
                    v-model="productFilter.title">
            </div>
            <div class="input-group w-full">
                <label for="price" class="text-teal-900">Price ৳{{ productFilter.price }}</label>
                <input type="range"
                    class="transparent h-1.5 w-full cursor-pointer appearance-none rounded-lg border-transparent bg-teal-200"
                    id="price" min="0" v-bind:max="`${heightProductPrice}`" v-model="productFilter.price" />
            </div>
            <div class="input-group w-full">
                <label for="price" class="text-teal-900 w-full">In Stock</label>
                <div class="flex flex-col items-start">
                    <div class="input-sub-group w-full">
                        <input type="radio" id="yes" value="1" class="w-fit mr-2" v-model="productFilter.total_stock">
                        <label class="w-fit text-teal-900" for="yes">Yes</label>
                    </div>
                    <div class="input-sub-group w-full">
                        <input type="radio" id="no" value="0" class="w-fit mr-2" v-model="productFilter.total_stock">
                        <label class="w-fit text-teal-900" for="no">No</label>
                    </div>
                    <div class="input-sub-group w-full">
                        <input type="radio" id="both" value="null" class="w-fit mr-2" v-model="productFilter.total_stock">
                        <label class="w-fit text-teal-900" for="both">Both</label>
                    </div>
                </div>
            </div>
            <div class="input-group w-full">
                <button class="bg-teal-900 text-teal-50 border-1 border-teal-950 px-5 py-2" type="submit">Apply</button>
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useElementStore from '../../stores/ElementsStore';
import useProductStore from '../../stores/ProductStore';
import useSettingsStore from '../../stores/SettingsStore';

const productStore = useProductStore()
const elementsStore = useElementStore();
const settingsStore = useSettingsStore();
const { showFilter } = storeToRefs(elementsStore);
const { productFilter } = storeToRefs(productStore);
const { heightProductPrice } = storeToRefs(settingsStore);


const applyFilterHandler = async (e: Event) => {
    // @ts-ignore
    const url = BACKEND_URL + "/products/filters/" + "?" + new URLSearchParams(productStore.sereliazedProductFilter).toString();
    console.log(url);
    await productStore.fetchFilteredProducts(url);
}


</script>

