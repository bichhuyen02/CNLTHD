from django.urls import path, include
from . import views

urlpatterns = [
    path('courses/', views.index, name="index"),
    path('courses/<int:course_id>', views.list, name="list"),
    path('categorise/', views.index, name="index")
]
