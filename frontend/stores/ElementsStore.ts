import { defineStore } from "pinia";
import { MenuInterface, RightMenuInterface, DashboardSidebarMenuInterface } from "types/ElementsSettingType";

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
            { id: 3, name: "simple-line-icons:user", text: "User Account", color: 'black', link: '/user/signin' },
            { id: 4, name: "heroicons-solid:arrow-right-on-rectangle", text: "Logout", color: 'black', link: '#' },
        ] as RightMenuInterface[],
        dashboardSidebar: [
            { id: 1, name: "bx:box", text: "Product" },
            { id: 2, name: "simple-line-icons:grid", text: "Category" },
            { id: 3, name: "et:gears", text: "Setting" },
            { id: 4, name: "simple-line-icons:handbag", text: "Order" },
            { id: 5, name: "simple-line-icons:user", text: "User" },
        ] as DashboardSidebarMenuInterface[],
        selectedDSID: 1 as number, // DSI = Dashboard Sidebar ID
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
        changeDSID(newDSID: number) {
            this.selectedDSID = newDSID;
        }
    }
});

export default useElementStore;