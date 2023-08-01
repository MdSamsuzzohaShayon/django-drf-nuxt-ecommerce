<template>
    <div>
        <header class="shadow-sm bg-white">
            <!-- MENU: 1 -> Top offer menu  -->
            <div class="top-offer-menu bg-teal-300 w-full ">
                <div class="container mx-auto px-2 py-2">
                    <p class="text-xs">Free Delivery on orders over £120. Don’t miss discount.</p>
                </div>
            </div>
            <!-- MENU: 2 -> Middle social menu  -->
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
            <!-- MENU: 3 -> Bottom main menu  -->
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
                            <NuxtLink v-bind:to="rm.link" v-else-if="rm.id === 3">
                                <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" />
                            </NuxtLink>
                            <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" v-else />
                        </li>
                    </ul>
                </nav>
            </div>
            <!-- SEARCH -> A search bar over the menu on an specific event  -->
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
import useUserStore from '../stores/UserStore';
import useCategoryStore from '../stores/CategoryStore';
// https://dev.to/rafaelmagalhaes/pinia-and-nuxt-3-4ij5

// Local State
const showSearchBar = ref<boolean>(false);
const searchInputEl = ref<HTMLInputElement | null>(null);
const state = reactive({ q: null })

// Pinia State
const categoryStore = useCategoryStore();
const settingsStore = useSettingsStore();
const elementsStore = useElementsStore();
const userStore = useUserStore();

const { logoUrl, socialLinks } = storeToRefs(settingsStore);
const { menus, rightMenus } = storeToRefs(elementsStore);
const { isAuthenticated } = storeToRefs(userStore);

const displaySearchBarHandler = (e: Event) => {
    showSearchBar.value = !showSearchBar.value;
    setTimeout(() => {
        if (searchInputEl.value) {
            searchInputEl.value.focus()
        }
    }, 500);

}

const searchHandler = async (e: Event) => {
    showSearchBar.value = !showSearchBar.value;
    await navigateTo(`/search/?q=${state.q}`);
}

defineExpose({ searchInputEl });


let refreshTokenCycle: any = null;

onMounted(async () => {
    const token = useCookie("token");

    const fetchAtBeginning = []
    if (!token || !token.value) {
        userStore.setIsAuthenticated(false);
    } else {
        // @ts-ignore
        const { access: accessBefore, refresh: refreshBefore } = token.value;
        // Get User from localStorage and set state 

        // Make a cyccle of request to use refresh token and get a new access token
        if (accessBefore && refreshBefore) {
            await userStore.setRefreshToken(refreshBefore);
            const tokenUpdate = useCookie("token");
            // @ts-ignore
            const { access: accessAfter, refresh: refreshAfter } = tokenUpdate.value;
            fetchAtBeginning.push(userStore.fetchUser(accessAfter));
            // Make a request to the server to get user informations
            // User user to localStorage

            // Refresh token in every 9 minuts
            refreshTokenCycle = setInterval(async () => {
                await userStore.setRefreshToken(refreshBefore);
            }, TOKEN_REFRESH_TIME);
        }
    }
    fetchAtBeginning.push(categoryStore.fetchCategories());
    await Promise.all(fetchAtBeginning);

});

onUnmounted(() => {
    console.log("Unmount default layout ", refreshTokenCycle);

    if (refreshTokenCycle) {
        clearInterval(refreshTokenCycle);
    }
});



</script>