import axios from "axios";

const HOST = "https://bichhuyen02.pythonanywhere.com"
// const HOST = "http://127.0.0.1:8000"

export const endpoints = {
    'categories': "/categories/",
    'bStation': "/bStation/",
    'province': "/province/",
    'provinceDetail': (province_id) =>`/province/${province_id}`,
    'provinceBsta': (province_id) =>`/province/${province_id}/bstation`,
    'buses': "/buses/",
    'trip': "/trips/",
    'tripDetail': (trip_id) => `/trip/${trip_id}/`,

    'invoice': '/invoice/',
    'bookTicket_onl': (trip_id) => `/trip/${trip_id}/ticket-onl`,


    
    'login': '/o/token/',
    'current_user': '/user/current-user/',
    'register': '/user/user/',
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