import axios from "axios";

const HOST = "https://bichhuyen02.pythonanywhere.com"

export const endpoints = {
    'categories': "/categories/",
    'categoryDetail': (category_id)=>`/categories/${category_id}/`,
    'carDetail': (car_id)=>`/cars/${car_id}/`,
    
    'bStation': "/bStation/",
    'bStationDetail': (bStation_id) =>`/bStation/${bStation_id}/`,
    'province': "/province/",
    'provinceDetail': (province_id) =>`/province/${province_id}/`,
    'provinceBsta': (province_id) =>`/province/${province_id}/bstation/`,
    'buses': "/buses/",
    'buesDetail': (bues_id) =>`/bues/${bues_id}/`,

    'trip': "/trips/",
    'tripDetail': (trip_id) => `/trip/${trip_id}/`,
    'tripDCar':(trip_id) =>`/trips/${trip_id}/tripCar/`,
    'tripCar': "/tripCar/",
    'tripCarDetail': (tripCar_id) => `/tripCar/${tripCar_id}/`,

    'complain': "/complain/",
    'complainT': (tripCar_id) =>`/tripCar/${tripCar_id}/add_complain/`,
    'complainDetail': (complain_id) =>`/complain/${complain_id}/`,

    'invoice': '/invoice/',
    'invoiceDetail': (invoice_id) =>`/invoice/${invoice_id}/`,
    'bookTicket_onl': (trip_id) => `/trip/${trip_id}/ticket-onl/`,
    'bookTicket': (trip_id) => `/trip/${trip_id}/ticket/`,
    'ticket': "/ticket/",
    'ticketDetail': (ticket_id) =>`/ticket/${ticket_id}/`,
    'ticketCustomer':(ticket_id) => `/customer/${ticket_id}/ticket/`,

    
    'login': '/o/token/',
    'current_user': '/user/current-user/',
    'register': '/user/user/',
    'customers': '/customer/',
}

export const authApi = (accessToken) => axios.create({
    baseURL: HOST,
    headers: {
        "Authorization": `Bearer ${accessToken}`
    }
})

export default axios.create({
    baseURL: HOST
})