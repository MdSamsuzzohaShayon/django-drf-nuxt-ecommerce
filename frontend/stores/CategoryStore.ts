import { defineStore } from "pinia";
import { ProductCategoryInterface } from "../types/ProductCategoryType";

const useCategoryStore = defineStore('categoryStore', {
    state: () => ({
        categoryList: [] as ProductCategoryInterface[],
        currentCategory: {} as ProductCategoryInterface,
    }),
    actions: {
        addNewCategory(newCategory: ProductCategoryInterface) {
            this.categoryList.push(newCategory);
        },
        deleteCategory(catId: number) {
            this.categoryList = this.categoryList.filter((c: ProductCategoryInterface) => c.id !== catId);
        },
        setCurrentCategory(catId: number) {
            const findItem = this.categoryList.find((c: ProductCategoryInterface) => c.id !== catId);
            if(findItem){
                this.currentCategory = findItem;
            }
        },
        async fetchCategories() {
            const { data: productCategories, refresh: refreshRequest } = await useFetch<ProductCategoryInterface[]>(`${BACKEND_URL}/products/categories/list/`);
            await refreshRequest();
            if (productCategories.value) {
                this.categoryList = productCategories.value
            }

        },
    }
});


export default useCategoryStore;