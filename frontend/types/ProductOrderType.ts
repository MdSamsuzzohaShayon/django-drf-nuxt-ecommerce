import { UserAddressInterface } from "./UserType";
import { ProductInterface } from './ProductType';

enum OrderStatus {
    PENDING = "PG",
    SHIPPING = "SG",
    COMPLETED = "CD",
    CANCELED = "CL",
}

interface OrderInterface {
    id: number;
    status: OrderStatus.PENDING | OrderStatus.SHIPPING | OrderStatus.COMPLETED | OrderStatus.CANCELED;
    is_paid: boolean;
    product: ProductInterface;
    address: UserAddressInterface;
    quantity: number;
    total: number;
}

interface OrganizedOrderInterface {
    id: number;
    status: string;
    is_paid: boolean;
    product: string;
    address: UserAddressInterface;
    quantity: number;
    total: number;
}


export {
    OrderStatus,
    OrderInterface,
    OrganizedOrderInterface
}