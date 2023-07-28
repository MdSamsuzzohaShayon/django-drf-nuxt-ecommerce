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
                    <ul class="flex justify-end list-none" >
                        <li v-for="rm in rightMenus" class="ml-4">
                            <Icon v-bind:name="rm.name" size="20" v-bind:color="rm.color" />
                        </li>
                    </ul>
                </nav>
            </div>
        </header>

        <!-- Output the page content  -->
        <slot />
    </div>
</template>

<script>
import { storeToRefs } from 'pinia';
import useSettingsStore from '../stores/SettingsStore';
import useElementsStore from '../stores/ElementsStore';
// ~/stores/myStore
export default {
    setup() {
        const settingsStore = useSettingsStore();
        const elementsStore = useElementsStore();
        const { logoUrl, socialLinks } = storeToRefs(settingsStore);
        const { menus, rightMenus } = storeToRefs(elementsStore);

        return {
            socialLinks,
            menus,
            rightMenus,
            logoUrl
        }
    }
}
</script>