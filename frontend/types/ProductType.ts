interface ProductBaseInterface {
    id: number;
    title: string;
    price: number;
    discount_price: number;
    total_stock: number;
    description: string;
    category: number;
}

interface ProductAddUpdateInterface {
    id?: number | null;
    title: string;
    price: number | null;
    discount_price: number | null;
    total_stock: number | null;
    description: string;
    category: number | null;
}

interface ProductInterface extends ProductBaseInterface {
    image1: string;
    image2: string | null;
    image3: string | null;
    image4: string | null;
    created_at: string;
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

interface CartItemInterface {
    id: string;
    pId: number;
    qty: number;
}

export {
    ProductBaseInterface,
    ProductInterface,
    ProductFilterInterface,
    ProductFilterOptionalInterface,
    CartItemInterface,
    ProductAddUpdateInterface
}