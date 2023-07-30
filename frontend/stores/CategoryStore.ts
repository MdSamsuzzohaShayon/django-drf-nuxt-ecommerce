import { defineStore } from "pinia";
import { ProductCategoryInterface } from "types/ProductCategoryType";

const useCategoryStore = defineStore('categoryStore', {
    state: ()=>({
        categoryList: [] as ProductCategoryInterface[]
    }),
    actions: {
        async fetchCategories(){
            const {data: productCategories} = await useFetch<ProductCategoryInterface[]>(`${BACKEND_URL}/products/categories/`);
            // console.log({productCategories, values: productCategories.value});
            
            if (productCategories.value){
                this.categoryList = productCategories.value
            }
            
        }
    }
});


export default useCategoryStore;