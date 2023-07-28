<template>
    <div class="relative">
        <!-- Display slider  -->
        <div class="new-arrival-wrapper relative" v-for="na in newArrivals">
            <div class="text-and-controls absolute top-0 left-0 flex justify-center items-center  flex-col w-full h-full"
                v-if="selectedProductId === na.id">
                <h1 class="text-4xl capitalize">{{ siteTitle }}</h1>
                <h2 class="text-sm">{{ na.title }}</h2>
                <button class="px-4 py-2 border-4 text-teal-950 border-teal-950">Shop Now</button>

                <div class="slider-controls">
                    <button class="border-0 bg-none">
                        <Icon name="simple-line-icons:arrow-left" size="20" color="black"
                            v-on:click.prevent="settingsStore.changeSliderItem(false)" />
                    </button>
                    <button class="border-0 bg-none">
                        <Icon name="simple-line-icons:arrow-right" size="20" color="black"
                            v-on:click.prevent="settingsStore.changeSliderItem(true)" />
                    </button>
                </div>
            </div>
            <div class="background-image w-full" v-if="selectedProductId === na.id">
                <img v-bind:src="na.image1" v-bind:alt="na.title" class="h-screen w-full object-center object-cover">
            </div>
        </div>

        <Category />
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useSettingsStore from '../stores/SettingsStore';



const settingsStore = useSettingsStore();
const { newArrivals, selectedProductId, siteTitle } = storeToRefs(settingsStore);

</script>

<style scoped></style>