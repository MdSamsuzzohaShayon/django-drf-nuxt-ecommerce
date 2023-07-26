<template>
    <div class="relative">
        <div class="new-arrival-wrapper relative" v-for="na in newArrivals" >
            <div class="text-and-controls absolute top-0 left-0">
                <h1>{{ na.title }}</h1>
            </div>
            <div class="background-image w-full">
                <img v-bind:src="na.image1" v-bind:alt="na.title" class="h-screen w-full object-center object-cover">
            </div>
        </div>
    </div>
</template>

<script>
import { storeToRefs } from 'pinia';
import useSettingsStore from '../stores/SettingsStore';
export default {
    setup() {

        const settingsStore = useSettingsStore();
        const { newArrivals } = storeToRefs(settingsStore);

        return {
            newArrivals
        }
    }
}

</script>

<style scoped></style>