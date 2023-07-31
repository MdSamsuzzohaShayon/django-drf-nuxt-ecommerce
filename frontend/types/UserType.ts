interface UserSigninInterface {
    email: string;
    password: string;
}

interface UserSignupInterface extends UserSigninInterface{
    first_name: string;
    last_name: string;
    email: string;
    password: string;
    confirm_password: string;
}

export {
    UserSignupInterface,
    UserSigninInterface
}