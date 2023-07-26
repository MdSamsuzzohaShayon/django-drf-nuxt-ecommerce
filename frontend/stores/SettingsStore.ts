import { defineStore } from "pinia";
import { SocialLinkInterface, NewArrivalInterface } from "types/SiteSettingsType";

const useSettingsStore = defineStore('settingsStore', {
    state: () => ({
        socialLinks: [
            { id: 1, name: "bxl:facebook", color: 'black', link: '' },
            { id: 2, name: "bxl:twitter", color: 'black', link: '' },
            { id: 3, name: "bxl:instagram", color: 'black', link: '' },
        ] as SocialLinkInterface[],
        logoUrl: "/logo.png" as string,
        newArrivals: [
            { id: 1, title: "Product 1", category: 1, description: "Desc", image1: "/img/bg-1.jpg" },
            { id: 2, title: "Product 2", category: 2, description: "Desc", image1: "/img/bg-2.jpg" },
            { id: 3, title: "Product 3", category: 1, description: "Desc", image1: "/img/bg-3.jpg" },
        ] as NewArrivalInterface[]
    })
});

export default useSettingsStore;