import { defineStore } from "pinia";
import { UserSignupInterface, UserSigninInterface, UserInfoInterface, UserAddressInterface } from '../types/UserType';

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
        isAuthenticated: false,
        userInfo: {
            id: null,
            email: null,
            first_name: null,
            last_name: null,
            is_admin: null,
            is_validated: null,
            is_staff: null,
            is_active: null,
            address: [] as UserAddressInterface[]
        } as UserInfoInterface,
        userList: [] as UserInfoInterface[]
    }),
    actions: {
        setIsAuthenticated(isAuthenticated: boolean) {
            this.isAuthenticated = isAuthenticated;
        },
        async setRefreshToken(refreshToken: string) {
            const { data: newRefreshToken, error: refreshError, refresh: refreshRequest, status: refreshStatus } = await useFetch(`${BACKEND_URL}/accounts/token/refresh/`, {
                key: `${new Date().getSeconds()}`,
                method: "POST",
                body: {
                    refresh: refreshToken
                }
            });
            await refreshRequest();

            if (refreshStatus.value === 'success') {
                const token = useCookie("token", {
                    maxAge: MAX_SIGNIN_COOKIE_AGE,
                    // httpOnly: true, // On https protocal, Need to set by server 
                });
                token.value = JSON.stringify(newRefreshToken.value);
            }

        },
        async fetchUser(accessToken: string) {

            const { data: userInfo, error: userError, refresh: refreshRequest, status: userStatus } = await useFetch<UserInfoInterface>(`${BACKEND_URL}/accounts/detail/`, {
                key: `${new Date().getSeconds()}`,
                headers: {
                    "Authorization": `Bearer ${accessToken}`
                }
            });
            await refreshRequest();
            console.log({ "Error ": userError.value, "Status": userStatus.value, "data": userInfo.value });

            if (userStatus.value === 'success' && userInfo.value) {
                this.isAuthenticated = true;
                this.userInfo = userInfo.value;
            }
        },
        async fetchAllUser(accessToken: string) {
            // accounts/list/
            const { data: userList, error: userError, refresh: refreshRequest, status: userStatus } = await useFetch<UserInfoInterface[]>(`${BACKEND_URL}/accounts/list/`, {
                key: `${new Date().getSeconds()}`,
                headers: {
                    "Authorization": `Bearer ${accessToken}`
                }
            });
            await refreshRequest();
            console.log({ "Error ": userError.value, "Status": userStatus.value, "data": userList.value });
            if (userStatus.value === 'success' &&  userList.value) {
                this.userList = userList.value;
            }
        }
    },
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