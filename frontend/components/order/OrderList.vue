<template>
    <div>
        <!-- orderList -->
        <table class="w-full mt-4">
            <thead>
                <tr>
                    <th class="p-2 text-center border border-teal-900">ID</th>
                    <th class="p-2 text-center border border-teal-900">Product</th>
                    <th class="p-2 text-center border border-teal-900">Status</th>
                    <th class="p-2 text-center border border-teal-900">Quantity</th>
                    <th class="p-2 text-center border border-teal-900">Address</th>
                    <th class="p-2 text-center border border-teal-900">Total Price (৳)</th>
                    <th class="p-2 text-center border border-teal-900">Perform</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="order in organizedOrders()">
                    <td class="p-2 text-center border border-teal-900/50">{{ order.id }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ order.product }}</td>
                    <td class="p-2 text-center border border-teal-900/50 capitalize">{{ order.status }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ order.quantity }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ `${order.address.area}, ${order.address.city},
                                            ${order.address.phone}` }}</td>
                    <td class="p-2 text-center border border-teal-900/50">{{ order.total }}</td>
                    <td class="p-2 text-center border border-teal-900/50">
                        <p class="cursor-pointer text-red-900" v-if="order.status === 'PENDING'"
                            v-on:click.prevent="cancelOrderHandler(order.id)">Cancel</p>
                        <NuxtLink v-bind:to="`#`">
                            <p class="cursor-pointer text-teal-900">View</p>
                        </NuxtLink>
                        <!-- <Icon class="pr-2" size="20" name="bytesize:eye" color="teal" /> -->
                        <p v-if="userInfo.is_staff" class="cursor-pointer text-teal-900"
                            v-on:click.prevent="updateOrderHandler(order.id)">Update</p>
                        <!-- <Icon v-if="userInfo.is_staff" class="pr-2" size="20" name="line-md:edit" v-on:click.prevent="updateOrderHandler(order.id)"
                            color="teal" /> -->
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';

import useOrderStore from '../../stores/OrderStore';
import useProductStore from '../../stores/ProductStore';
import useUserStore from '../../stores/UserStore';
import { OrderStatus, OrganizedOrderInterface, OrderInterface } from '../../types/ProductOrderType';

const ordersStore = useOrderStore();
const productStore = useProductStore();
const userStore = useUserStore();

const { orderList } = storeToRefs(ordersStore);
const { userInfo } = storeToRefs(userStore);

const cancelOrderHandler = async (oId: number | null) => {
    const token = useCookie('token');
    // @ts-ignore
    const { access: accessToken } = token.value;
    const { data: orderData, error: orderError, refresh: orderRefresh, status: orderStatus } = await useFetch(`${BACKEND_URL}/orders/cancel/${oId}/`, {
        key: oId + '-' + new Date().getSeconds() + '-' + new Date().getMilliseconds(),
        method: "PUT",
        headers: {
            "Authorization": `Bearer ${accessToken}`
        }
    });
    if (orderStatus.value === 'success' && orderData.value) {
        if (oId) ordersStore.cancelAnOrder(oId);
    }
}

const updateOrderHandler = (oId: number) => {
    // ordersStore.setOrderUpdate(true);
    // ordersStore.setOrderToUpdate(pId);
}



const organizedOrders = () => {
    const newOrderList: OrganizedOrderInterface[] = [];
    const ol = orderList.value;
    for (let i = 0; i < ol.length; i++) {
        // product: number;
        // address: number;
        let status = "PENDING";
        if (ol[i].status === OrderStatus.COMPLETED) {
            status = "COMPLETED";
        } else if (ol[i].status === OrderStatus.SHIPPING) {
            status = "SHIPPING";
        } else if (ol[i].status === OrderStatus.CANCELED) {
            status = "CANCELED";
        }

        // const findProduct = productStore.productList.find(p => p.id === ol[i].product);
        // console.log(userInfo.value.address[i]);

        const newOrder: OrganizedOrderInterface = {
            id: ol[i].id,
            status: status,
            is_paid: ol[i].is_paid,
            product: ol[i].product.title,
            quantity: ol[i].quantity,
            // address: `${userInfo.value.address[0]?.area}, ${userInfo.value.address[0]?.city}`,
            address: ol[i].address,
            total: ol[i].total,
        }
        newOrderList.push(newOrder);
    }
    return newOrderList;
}

</script>

<style scoped></style>