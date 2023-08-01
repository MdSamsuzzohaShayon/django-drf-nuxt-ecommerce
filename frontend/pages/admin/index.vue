<template>
    <div class="container mx-auto px-2">
        <h2>Admin Panel</h2>
        <div class="flex justify-between">
            <div class="left-side bar w-2/12">
                <ul class="h-screen w-full bg-teal-100 h-screen">
                    <li v-for="dsi in dashboardSidebar" v-on:click.prevent="elementStore.changeDSID(dsi.id)"
                        class="bg-teal-700 border-1 border-teal-950 text-teal-100 flex justify-start items-ceonter gap-2 p-2 cursor-pointer">
                        <Icon v-bind:name="dsi.name" size="20" />
                        <p class="capitalize">{{ dsi.text }}</p>
                    </li>
                </ul>
            </div>
            <div class="content w-10/12">
                <div class="selected-item" v-if="selectedDSID === 1">
                    <h2>Product</h2>
                    <ProductAdd />
                    <ProductList />
                </div>
                <div class="selected-item" v-else-if="selectedDSID === 2">
                    <h2>Category</h2>
                    <CategoryAdd />
                    <CategoryList />
                </div>
                <div class="selected-item" v-else-if="selectedDSID === 3">
                    <h2>Setting</h2>
                    <SettingAdd />
                </div>
                <div class="selected-item" v-else-if="selectedDSID === 4">
                    <h2>Order</h2>
                    <OrderDetail />
                    <OrderList />
                </div>
                <div class="selected-item" v-else-if="selectedDSID === 5">
                    <h2>User</h2>
                    <UserList />
                    <UserDetail />
                </div>
            </div>
        </div>
        <p class="text-red-900 px-4 py-2 capitalize" v-for="message in errorMessageList">{{ message }}</p>
        <p class="text-teal-900 px-4 py-2 capitalize" v-for="message in successMessageList">{{ message }}</p>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useUserStore from '../../stores/UserStore';
import useElementStore from '../../stores/ElementsStore';

const userStore = useUserStore();
const elementStore = useElementStore();

const { isAuthenticated } = storeToRefs(userStore);
const { dashboardSidebar, selectedDSID, errorMessageList, successMessageList } = storeToRefs(elementStore);


onMounted(() => {
    if (isAuthenticated.value === false) {
        // Check role
        navigateTo('/admin/signin/');
    }
});
</script>

<style lang="scss" scoped></style>