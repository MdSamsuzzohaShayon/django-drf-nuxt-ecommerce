interface MenuInterface {
    id: number;
    text: string;
    link: string;
}

interface RightMenuInterface {
    id: number;
    name: string;
    text: string;
    color: string;
    link: string;
}


interface SidebarMenuInterface {
    id: number;
    name: string;
    text: string;
}

export {
    MenuInterface,
    RightMenuInterface,
    SidebarMenuInterface
};