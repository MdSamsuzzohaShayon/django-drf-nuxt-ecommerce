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
            { id: 1, name: "simple-line-icons:magnifier", text:"Search", color: 'black'},
            { id: 2, name: "simple-line-icons:basket", text:"Cart", color: 'black'},
            { id: 3, name: "simple-line-icons:user", text:"User Account", color: 'black'},
        ] as RightMenuInterface[]
    }),
});

export default useElementStore;