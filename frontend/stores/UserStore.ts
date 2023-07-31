import { defineStore } from "pinia";
import { UserSignupInterface, UserSigninInterface } from '../types/UserType';

const useUserStore = defineStore('userStore', {
    state: () => ({
        userSignup: {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            confirm_password: '',
        } as UserSignupInterface,
        userSignin: {
            email: '',
            password: '',
        } as UserSigninInterface,
    }),
    getters: {
        serializedUserSignup(state): UserSignupInterface | null {
            const userSignupData: UserSignupInterface = {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                confirm_password: '',
            }
            let isValid = true;
            for (const [k, v] of Object.entries(state.userSignup)) {
                if (v === '' || v === undefined || v === null) {
                    isValid = false;
                } else {
                    userSignupData[k as keyof UserSignupInterface] = v;
                }
            }
            if (userSignupData.password !== userSignupData.confirm_password) {
                isValid = false;
            }
            if (isValid) return userSignupData;
            return null;
        },
        serializedUserSignin(state): UserSigninInterface | null {
            const userSigninData: UserSigninInterface = {
                email: '',
                password: '',
            }
            let isValid = true;
            for (const [k, v] of Object.entries(state.userSignin)) {
                if (v === '' || v === undefined || v === null) {
                    isValid = false;
                } else {
                    userSigninData[k as keyof UserSigninInterface] = v;
                }
            }
            if (isValid) return userSigninData;
            return null;
        }
    }
});

export default useUserStore;