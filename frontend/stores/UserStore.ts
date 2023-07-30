import { defineStore } from "pinia";
import { UserSignupInterface } from '../types/UserType';

const useUserStore = defineStore('userStore', {
    state: () => ({
        userSignup: {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            confirm_password: '',
        } as UserSignupInterface,
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
            if (isValid) return userSignupData;
            return null
        }
    }
});

export default useUserStore;