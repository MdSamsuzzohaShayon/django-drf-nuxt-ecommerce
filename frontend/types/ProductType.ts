interface ProductInterface {
    id: number;
    title: string;
    price: number;
    discount_price: number;
    total_stock: number;
    description: string;
    image1: string | null;
    image2: string | null;
    image3: string | null;
    image4: string | null;
    created_at: string;
    category: number
}

interface ProductFilterInterface {
    title: string | null;
    price: string | null;
    total_stock: string | null;
    category: number | null;
}

interface ProductFilterOptionalInterface {
    title?: string;
    price?: number;
    total_stock?: number;
    category?: number;
}

export {
    ProductInterface,
    ProductFilterInterface,
    ProductFilterOptionalInterface
}