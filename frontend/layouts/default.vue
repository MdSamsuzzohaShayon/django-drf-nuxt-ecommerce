<template>
    <div>
        <header class="shadow-sm bg-white">
            <div class="top-offer-menu bg-teal-300 w-full ">
                <div class="container mx-auto px-2 py-2">
                    <p class="text-xs">Free Delivery on orders over £120. Don’t miss discount.</p>
                </div>
            </div>
            <div class="middle-social-menu bg-white text-teal-950 border-b border-teal-90">
                <div class="container mx-auto px-2 py-2">
                    <ul class="flex justify-start">
                        <li v-for="link in socialLinks">
                            <NuxtLink v-bind:to="link.link">
                                <Icon v-bind:name="link.name" size="20" color="black" />
                            </NuxtLink>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="bottom-main-menu container mx-auto px-2 py-6 flex justify-between">
                <nav class=" w-1/3">
                    <ul class="flex justify-start list-none">
                        <li class="mr-4" v-for="menu in menus">
                            <NuxtLink v-bind:to="menu.link" class="uppercase">{{ menu.text }}</NuxtLink>
                        </li>
                    </ul>
                </nav>
                <div class="flex justify-center w-1/3">
                    <NuxtLink to="/"><img v-bind:src="logoUrl" alt="" class="h-8"></NuxtLink>
                </div>
                <nav class="w-1/3">
                    <ul class="flex justify-end list-none">
                        <li v-for="rm in rightMenus" class="ml-4">
                            <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" v-if="rm.id === 1"
                                v-on:click.prevent="displaySearchBarHandler" />
                            <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" v-else />
                        </li>
                    </ul>
                </nav>
            </div>
            <div class="search-bar-menu bg-white text-teal-950 absolute top-0 left-0 w-full z-20"
                v-if="showSearchBar === true">
                <div class="container mx-auto px-2 py-6 flex justify-between items-center">
                    <form class="flex items-center justify-center" v-on:submit.prevent="searchHandler">
                        <button type="submit" class="px-4">
                            <Icon size="20" name="simple-line-icons:magnifier" class="text-teal-950" />
                        </button>
                        <input type="text" id="search-text" class="bg-real-100 text-teal-950 outline-0 text-3xl capitalize"
                            placeholder="Search...." ref="searchInputEl" v-model="state.q">
                    </form>
                    <div class="close-button">
                        <Icon name="grommet-icons:close" size="20" class="text-teal-950"
                            v-on:click.prevent="showSearchBar = !showSearchBar" />
                    </div>
                </div>
            </div>
        </header>

        <div class="whole-display-overflow absolute h-full w-full bg-teal-950 z-10 opacity-70 left-0 top-0 "
            v-bind:class="showSearchBar ? 'block' : 'hidden'"></div>

        <!-- Output the page content  -->
        <slot />
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useSettingsStore from '../stores/SettingsStore';
import useElementsStore from '../stores/ElementsStore';

// const router = useRouter();

const showSearchBar = ref<boolean>(false);
const searchInputEl = ref<HTMLInputElement | null>(null);
const state = reactive({ q: null })
// const state = reactive({ count: 0 })


// ~/stores/myStore
const settingsStore = useSettingsStore();
const elementsStore = useElementsStore();
const { logoUrl, socialLinks } = storeToRefs(settingsStore);
const { menus, rightMenus } = storeToRefs(elementsStore);

const displaySearchBarHandler = (e: Event) => {
    showSearchBar.value = !showSearchBar.value;
    setTimeout(() => {
        // input type="text"
        // const searchInputEl = document.querySelector("input[type='text']");
        // const searchInputEl = document.getElementById("search-text");
        // console.log(searchInputEl.value);
        if (searchInputEl.value) {
            searchInputEl.value.focus()
        }
    }, 500);

}

const searchHandler = async (e: Event) => {
    showSearchBar.value = !showSearchBar.value;
    // console.log(state);

    await navigateTo(`/search/?q=${state.q}`);

}

defineExpose({ searchInputEl });

watch(searchInputEl, (searchInputEl, prevSearchInputEl) => {
    console.log({val: searchInputEl?.value, prevVal: prevSearchInputEl?.value});
})
</script>