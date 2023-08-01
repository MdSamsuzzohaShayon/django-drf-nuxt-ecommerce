import { defineStore } from "pinia";
import { ProductCategoryInterface } from "types/ProductCategoryType";

const useCategoryStore = defineStore('categoryStore', {
    state: ()=>({
        categoryList: [] as ProductCategoryInterface[]
    }),
    actions: {
        async fetchCategories(){
            const {data: productCategories, refresh: refreshRequest} = await useFetch<ProductCategoryInterface[]>(`${BACKEND_URL}/products/categories/`);
            console.log(productCategories.value);
            
            
            if (productCategories.value){
                this.categoryList = productCategories.value
            }
            await refreshRequest();
            
        }
    }
});


export default useCategoryStore;