// const { data: products } = await useFetch('http://localhost:8000/api/products/');
import { defineStore } from "pinia";
import { ProductInterface } from '../types/ProductType';

const useProductStore = defineStore('productStore', {
    state: () => ({
        productList: [] as ProductInterface[]
    }),
    actions: {
        async fetchProducts(q: string | null) {
            let url = `${BACKEND_URL}/products/`;
            if (q !== null || q !== '') {
                url = `${BACKEND_URL}/products/?search=${q}`;
            }
            const { data: products } = await useFetch<ProductInterface[]>(url);
            if (products.value) {
                this.productList = products.value;
            }
        },

        async fetchProductsByCategory(catId: number) {
            const { data: products } = await useFetch<ProductInterface[]>(`${BACKEND_URL}/products/categories/${catId}`);
            if (products.value) {
                this.productList = products.value;
            }
        },
    }
});


export default useProductStore;