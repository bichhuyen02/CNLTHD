import axios from "axios";

const HOST = "http://127.0.0.1:8000"

export const endpoints = {
    'courses': "/courses/",
    'categories': "/categories/",
    'lessons': (course_Id) => `/courses/${course_Id}/lessons/`,
    'lessonDetail': (lessonId) => `/lessons/${lessonId}/`,
    'login': '/o/token/',
    'current_user': '/users/current_user/',
    'register': '/users/',
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