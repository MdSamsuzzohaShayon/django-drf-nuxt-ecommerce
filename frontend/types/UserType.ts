interface UserSigninInterface {
    email: string;
    password: string;
}

interface UserSignupInterface extends UserSigninInterface {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
    confirm_password: string;
}

interface UserAddressInterface {
    id: number;
    city: string;
    country: string;
    phone: number;
    area: string;
    user: number;
}

interface AddressAddUpdateInterface {
    id?: number;
    city: string;
    country: string;
    phone: number | null;
    area: string;
    user: number;
}

interface UserInfoInterface {
    id: number | null;
    email: string | null;
    first_name: string | null;
    last_name: string | null;
    is_admin: boolean | null;
    is_validated: boolean | null;
    is_staff: boolean | null;
    is_active: boolean | null;
    address: UserAddressInterface[];
}

interface UserTokenInterface{
    access: string;
    refresh: string;
}

interface UserRequestSuccessResInt{
    detail: string;
}


export {
    UserSignupInterface,
    UserSigninInterface,
    UserInfoInterface,
    UserAddressInterface,
    AddressAddUpdateInterface,
    UserTokenInterface,
    UserRequestSuccessResInt
}