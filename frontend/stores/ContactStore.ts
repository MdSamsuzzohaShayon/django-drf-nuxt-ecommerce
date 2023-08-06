import { defineStore } from "pinia";
import { WillContactInterface, ContactFetchedInterface } from "../types/ContactType";

const useContactStore = defineStore('contactStore', {
    state: () => ({
        willContact: {
            name: '',
            email: '',
            message: ''
        } as WillContactInterface,
        contactList: [] as ContactFetchedInterface[],
        organizedContactList: [] as ContactFetchedInterface[],
    }),
    actions: {
        deleteContact(catId: number) {
            this.contactList = this.contactList.filter((c: ContactFetchedInterface) => c.id !== catId);
        },
        async fetchContacts(access: string) {
            const { data: productContacts, refresh: refreshRequest } = await useFetch<ContactFetchedInterface[]>(`${BACKEND_URL}/contacts/user/`, {
                headers: {
                    "Authorization": "Bearer " + access
                }
            });
            await refreshRequest();
            // console.log(productContacts.value);


            if (productContacts.value) {
                this.contactList = productContacts.value
            }

        },
    },
    getters: {
    }
});


export default useContactStore;