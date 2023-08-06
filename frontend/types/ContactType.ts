interface ContactBaseInterface {
    name: string;
    email: string;
    message: string;
}

interface WillContactInterface extends ContactBaseInterface {}

interface ContactFetchedInterface extends ContactBaseInterface{
    id: number;
}

export {
    WillContactInterface,
    ContactFetchedInterface
}