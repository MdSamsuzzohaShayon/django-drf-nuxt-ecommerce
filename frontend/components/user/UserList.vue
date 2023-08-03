<template>
    <div>
        <h1>User List</h1>
        <table class="table-auto w-full">
            <thead >
                <tr>
                    <th class="p-2 text-center border-4 border-teal-500" >ID</th>
                    <th class="p-2 text-center border-4 border-teal-500" >Name</th>
                    <th class="p-2 text-center border-4 border-teal-500" >Phone</th>
                    <th class="p-2 text-center border-4 border-teal-500" >Address</th>
                    <th class="p-2 text-center border-4 border-teal-500" >Verified</th>
                    <th class="p-2 text-center border-4 border-teal-500" >Admin</th>
                    <th class="p-2 text-center border-4 border-teal-500" >#</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in userList">
                    <td class="p-2 text-center border-2 border-teal-500">{{ user.id }}</td>
                    <td class="p-2 text-center border-2 border-teal-500">{{ user.first_name + " " + user.last_name }}</td>
                    <td class="p-2 text-center border-2 border-teal-500">01785208590</td>
                    <td class="p-2 text-center border-2 border-teal-500">West Raja Bazaar, Dhaka, Bangladesh</td>
                    <td class="p-2 text-center border-2 border-teal-500">
                        <Icon name="line-md:confirm" size="10" v-if="user.is_active" />
                    </td>
                    <td class="p-2 text-center border-2 border-teal-500">
                        <Icon name="line-md:confirm" size="10" v-if="user.is_admin || user.is_staff" />
                    </td>
                    <td class="p-2 text-center border-2 border-teal-500">
                        <Icon size="20" name="lucide:trash-2" color="red" v-on:click.prevent="deleteUserHandler(user.id)" />
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useUserStore from '../../stores/UserStore';

const userStore = useUserStore();

const { userList } = storeToRefs(userStore);

const deleteUserHandler = (uId: number | null) => {
    console.log("Delete user -> ", uId);
}

onMounted(async () => {
    const token = useCookie('token');
    // @ts-ignore
    const { access } = token.value;
    if (access) {
        await userStore.fetchAllUser(access);
    }
});
</script>

<style scoped></style>