import axios from "axios";

const HOST = "https://bichhuyen02.pythonanywhere.com"

export const endpoints = {
    'categories': "/categories/",
    'chair': (car_id) => `/cars/${car_id}/chair/`,

    'bStation': "/bStation/",
    'buses': "/buses/",
  
    'trip': "/trips/",
    'tripDetail': (trip_id) => `/trips/${trip_id}/`,

    'invoice': `/invoice/`,
    'invoice_ticket':(invoice_id)=>`/invoice/${invoice_id}/ticket/`,
    'bookTicket_onl': (trip_id) => `/trips/${trip_id}/ticket-onl/`,


    'login': '/o/token/',
    'current_user': '/user/current-user/',
    'register': '/user/',
    'comments': (lessonId) => `/lessons/${lessonId}/comments/`
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