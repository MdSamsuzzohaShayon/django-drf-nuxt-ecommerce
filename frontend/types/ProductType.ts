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

export {
    ProductInterface
}