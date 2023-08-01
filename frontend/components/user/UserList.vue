<template>
    <div>
        <h1>User List</h1>
        <ul>
            <li v-for="user in userList" class="flex justify-between bg-teal-100 mb-2 p-2">
                <p class="w-2/12" >{{ user.id }}</p>
                <p class="w-2/12" >{{ user.first_name + " " + user.last_name }}</p>
                <p class="w-2/12" >{{ user.is_active ? "Active" : 'Not Active' }}</p>
                <p class="w-2/12" >{{ user.is_admin || user.is_staff ? 'Admin' : 'User' }}</p>
                <Icon size="20" name="lucide:trash-2" color="red" v-on:click.prevent="deleteUserHandler(user.id)" />
            </li>
        </ul>
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