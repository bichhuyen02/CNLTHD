from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics
from .models import Course, User, Lesson, Tag, Category
from .serializers import CourseSerializer, LessonSerializer, TagSerializer, CategorySerializer
from .paginator import CoursePaginator


def index(request):
    return HttpResponse("e-Course App")


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CoursePaginator


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePaginator


class LessonViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePaginator


class TagViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Tag.objects.filter(active=True)
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePaginator


class CategoryView(View):
    pass