import axios from "axios";

const HOST = "https://bichhuyen02.pythonanywhere.com"

export const endpoints = {
    'courses': "/courses/",
    'categories': "/categories/",
    'lessons': (course_Id) => `/courses/${course_Id}/lessons/`,
    'lessonDetail': (lessonId) => `/lessons/${lessonId}/`,
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