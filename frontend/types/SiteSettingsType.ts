interface SocialLinkInterface{
    id: number,
    name: string,
    color: string,
    link: string
}

interface NewArrivalInterface{
    id: number;
    title: string;
    category: number;
    description: string;
    image1: string
}

export {
    SocialLinkInterface,
    NewArrivalInterface
}