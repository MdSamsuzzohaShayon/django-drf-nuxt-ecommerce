<template>
    <div>
        <h1>Category List</h1>
        <ul>
            <li v-for="cat in categoryList" class="flex justify-between bg-teal-100 mb-2 p-2">
                <p>{{ cat.name }}</p>
                <Icon size="20" name="lucide:trash-2" color="red" v-on:click.prevent="deleteCategoryHandler(cat.id)" />
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import useCategoryStore from '../../stores/CategoryStore';
import useElementStore from '../../stores/ElementsStore';

const categoryStore = useCategoryStore();
const elementStore = useElementStore();

const { categoryList } = storeToRefs(categoryStore);

const deleteCategoryHandler = async (catId: number) => {
    console.log("Delete category -> ", catId);
    const token = useCookie('token');
    if (!token.value) return null;
    // @ts-ignore
    const { access: accessToken } = token.value;
    // http://localhost:8000/api/products/categories/4/delete/
    const { data: catInfo, error: catError, refresh: refreshRequest, status: catStatus } = await useFetch(`${BACKEND_URL}/products/categories/${catId}/delete/`, {
        method: "DELETE",
        key: `${catId}`,
        headers: {
            "Authorization": `Bearer ${accessToken}`
        }
    });
    // await refreshRequest();
    // console.log({ "Error ": catError.value, "Status": catStatus.value, "data": catInfo.value });
    console.log(catError.value?.data);
    

    if (catStatus.value === 'success') {
        categoryStore.deleteCategory(catId);
    } else if (catStatus.value === 'error') {
        if(catError.value){
            // @ts-ignore
            elementStore.setErrorMessageList(Object.values(catError.value.data));
        }else{
            elementStore.setErrorMessageList(["Make sure to delete all the products containing this category before deleteting this!"]);
        }
    }
}


onMounted(async () => {
    // Reset error list
    elementStore.resetErrorMessageList();
    // fetchCategories
});
</script>

<style scoped></style>