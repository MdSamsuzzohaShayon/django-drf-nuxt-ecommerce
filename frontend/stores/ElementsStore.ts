import { defineStore } from "pinia";
import { MenuInterface, RightMenuInterface } from "types/ElementsSettingType";

const useElementStore = defineStore("elementsStore", {
    state: () => ({
        menus: [
            { id: 1, text: 'Home', link: "/" },
            { id: 2, text: 'About', link: "/about" },
            { id: 3, text: 'Contact', link: "/contact" },
        ] as MenuInterface[],
        rightMenus: [
            { id: 1, name: "simple-line-icons:magnifier", text: "Search", color: 'black', link: '#' },
            { id: 2, name: "simple-line-icons:basket", text: "Cart", color: 'black', link: '/cart' },
            { id: 3, name: "simple-line-icons:user", text: "User Account", color: 'black', link: '/user/signup' },
        ] as RightMenuInterface[],
        errorMessageList: [] as string[],
        successMessageList: [] as string[],
        isLoading: false as boolean,
        showFilter: false as boolean
    }),
    actions: {
        openFilterBar() {
            this.showFilter = true;
        },
        closeFilterBar() {
            this.showFilter = false;
        },
        setErrorMessageList(messageList: string[]) {
            this.errorMessageList = messageList;
        },
        resetErrorMessageList() {
            this.errorMessageList = [];
        },
        setSuccessMessageList(messageList: string[]) {
            this.successMessageList = messageList;
        },
        resetSuccessMessageList() {
            this.successMessageList = [];
        },
    }
});

export default useElementStore;