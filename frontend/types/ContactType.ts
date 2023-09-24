interface ContactBaseInterface {
    name: string;
    email: string;
    message: string;
}

interface WillContactInterface extends ContactBaseInterface {}

interface ContactFetchedInterface extends ContactBaseInterface{
    id: number;
    created_at: string;
    updated_at: string;
}

export {
    WillContactInterface,
    ContactFetchedInterface
}