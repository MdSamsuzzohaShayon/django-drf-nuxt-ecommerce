import { defineStore } from "pinia";
import { DeliveryPlaceInt } from "~/types/DeliveryPlaceType";

const useDeliveryPlaceStore = defineStore("deliveryPlace", {
  state: () => ({
    currentDeliveryPlace: {} as DeliveryPlaceInt,
    deliveryPlaceList: [] as DeliveryPlaceInt[],
  }),
  actions: {
    async fetchAllPlaces() {
      const { data: placeData, refresh: refreshRequest } = await useFetch<
        DeliveryPlaceInt[]
      >(`${BACKEND_URL}/products/delivery/list/`, {
        key: `order-list-${new Date().getSeconds()}-${new Date().getMilliseconds()}`,
        headers: {
          "Content-Type": "application/json",
        },
      });
      await refreshRequest();
      if (placeData.value) {
        this.deliveryPlaceList = placeData.value;
      }
    },
  },
});


export default useDeliveryPlaceStore;
