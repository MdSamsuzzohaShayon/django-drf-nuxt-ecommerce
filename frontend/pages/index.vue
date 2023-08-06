<template>
    <div class="relative">
        <!-- Display slider  -->
        <div class="new-arrival-wrapper" v-for="(na, index) in newArrivals" v-bind:key="index">
            <div class="single-arrival-item static md:relative h-fit md:h-screen " v-if="selectedProductId === na.id">
                <div class="background-image w-full static md:absolute top-0 left-0 z-0">
                    <img v-bind:src="na.image1" v-bind:alt="na.title"
                        class="h-80 md:h-screen w-full object-center object-cover">
                </div>
                <div
                    class="text-and-controls static md:absolute top-0 left-0 flex justify-center items-center  flex-col w-full h-full z-10">
                    <h1 class="text-4xl capitalize font-normal text-4xl leading-6 pt-8 md:pt-0">{{ siteTitle }}</h1>
                    <h2 class="text-sm mt-4">{{ na.title }}</h2>
                    <NuxtLink to="/products/">
                        <button
                            class="px-4 py-2 mt-4 border text-teal-950 border-teal-950 hover:text-teal-50 hover:bg-teal-950">Shop
                            Now</button>
                    </NuxtLink>

                    <div class="slider-controls mt-4 md:mt-32">
                        <button class="border-0 bg-none mr-32">
                            <Icon name="simple-line-icons:arrow-left" size="20" color="black"
                                v-on:click.prevent="settingsStore.changeSliderItem(false)" />
                        </button>
                        <button class="border-0 bg-none">
                            <Icon name="simple-line-icons:arrow-right" size="20" color="black"
                                v-on:click.prevent="settingsStore.changeSliderItem(true)" />
                        </button>
                    </div>
                </div>
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