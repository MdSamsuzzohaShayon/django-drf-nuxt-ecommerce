import { UserAddressInterface } from "./UserType";

enum OrderStatus {
    PENDING = "PG",
    SHIPPING = "SG",
    COMPLETED = "CD",
}

interface OrderInterface {
    id: number;
    status: OrderStatus.PENDING | OrderStatus.SHIPPING | OrderStatus.COMPLETED;
    is_paid: boolean;
    product: number;
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