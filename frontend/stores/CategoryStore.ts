import { defineStore } from "pinia";
import { ProductCategoryInterface } from "../types/ProductCategoryType";

const useCategoryStore = defineStore('categoryStore', {
    state: () => ({
        categoryList: [] as ProductCategoryInterface[]
    }),
    actions: {
        async fetchCategories() {
            const { data: productCategories, refresh: refreshRequest } = await useFetch<ProductCategoryInterface[]>(`${BACKEND_URL}/products/categories/`);
            await refreshRequest();
            console.log(productCategories.value);


            if (productCategories.value) {
                this.categoryList = productCategories.value
            }

        },
        addNewCategory(newCategory: ProductCategoryInterface){
            this.categoryList.push(newCategory);
        },
        deleteCategory(catId: number) {
            this.categoryList = this.categoryList.filter((c: ProductCategoryInterface) => c.id !== catId);
        }
    }
});


export default useCategoryStore;