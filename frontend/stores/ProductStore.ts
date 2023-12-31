// const { data: products } = await useFetch('http://localhost:8000/api/products/');
import { defineStore } from "pinia";
import { ProductInterface, ProductFilterInterface, ProductFilterOptionalInterface } from '../types/ProductType';

const useProductStore = defineStore('productStore', {
    state: () => ({
        productList: [] as ProductInterface[],
        productFilter: {
            title: null,
            price: '1200',
            total_stock: null,
            category: null
        } as ProductFilterInterface,
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
        async fetchFilteredProducts(url: string) {
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
    },
    getters: {
        sereliazedProductFilter(state): ProductFilterOptionalInterface {
            const newObj: ProductFilterOptionalInterface = {}
            // state.productFilter
            if (state.productFilter.title && state.productFilter.title !== 'null' && state.productFilter.title !== '') {
                newObj.title = state.productFilter.title.toString();
            }
            if (state.productFilter.price && state.productFilter.price !== 'null' && state.productFilter.price !== '') {
                newObj.price = parseInt(state.productFilter.price, 10);
            }
            if (state.productFilter.total_stock !== null || state.productFilter.total_stock !== 'null' || state.productFilter.total_stock !== '') {
                if (state.productFilter.total_stock === '1') {
                    newObj.total_stock = 1;
                } else if (state.productFilter.total_stock === '0') {
                    newObj.total_stock = 0
                }
            }
            return newObj;
        }
    }
});


export default useProductStore;