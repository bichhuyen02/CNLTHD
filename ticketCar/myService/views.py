from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Xe, LoaiXe, Ghe, GiaVe, BenXe, ChuyenXe, User, NhanVien, KhachHang, Complain, TaiXe
from rest_framework import viewsets, generics, status, permissions, parsers
from .paginator import CoursePaginator
# from . import perms
from .serializers import LoaiXeSerializer, XeSerializer, GheSerializer, GiaVeSerializer, BenXeSerializer, \
    ChuyenXeSerializer, UserSerializer, TaiXeSerializer, KhachHangSerializer, NhanVienSerializer, ComplainSerializer





#xe
class LoaiXeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = LoaiXe.objects.all()
    serializer_class = LoaiXeSerializer

class XeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Xe.objects.all()
    serializer_class = XeSerializer
    # pagination_class = CoursePaginator
    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     queries = self.queryset
    #     q = self.request.query_params.get('q')
    #     if q:
    #         queries = queries.filter(subject__icontains=q)
    #     return queries
    #
    # @action(methods=['get'],detail=True)
    # def lessons(self, request, pk):
    #     l = self.get_object().lesson_set.all()
    #     return Response(LessonSerializer(l, many=True, context={
    #         'request': request
    #     }).data, status=status.HTTP_200_OK)

class GheViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Ghe.objects.all()
    serializer_class = GheSerializer
    # permission_classes = [permissions.AllowAny()]

    # def get_permissions(self):
    #     if self.action in ['add_comment', 'like']:
    #         return [permissions.IsAuthenticated()]
    #     return self.permission_classes
    #
    # @action(methods=['post'], url_path="comments", detail=True)
    # def add_comment(self, request, pk):
    #     comment = Comment.objects.create(user=request.user, lesson = self.get_object(), content=request.data.get('content'))
    #     comment.save()
    #
    #     return Response(CommentSerializer(comment, context={
    #         'request': request
    #     }).data, status=status.HTTP_201_CREATED)
    #
    # @action(methods=['post'], url_path='like', detail=True)
    # def like(self, request, pk):
    #     like,create = Like.objects.get_or_create(user=request.user, lesson=self.get_object())
    #     if not create:
    #         like.liked = not like.liked
    #         like.save()
    #
    #     return Response(LessonSerializeDetail(self.get_object(),context={
    #         "request": request
    #     }).data, status=status.HTTP_200_OK)



#ve
class GiaVeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = GiaVe.objects.all()
    serializer_class = GiaVeSerializer

class VeViewSet(viewsets.ViewSet, generics.ListAPIView):
    pass
    # queryset = Ve.objects.all()
    # serializer_class = VeSerializer
    # pagination_class = CoursePaginator
    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     queries = self.queryset
    #     q = self.request.query_params.get('q')
    #     if q:
    #         queries = queries.filter(subject__icontains=q)
    #     return queries
    #
    # @action(methods=['get'],detail=True)
    # def lessons(self, request, pk):
    #     l = self.get_object().lesson_set.all()
    #     return Response(LessonSerializer(l, many=True, context={
    #         'request': request
    #     }).data, status=status.HTTP_200_OK)



#chuyen xe
class BenXeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = BenXe.objects.all()
    serializer_class = BenXeSerializer
    # pagination_class = CoursePaginator
    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     queries = self.queryset
    #     q = self.request.query_params.get('q')
    #     if q:
    #         queries = queries.filter(subject__icontains=q)
    #     return queries
    #
    # @action(methods=['get'],detail=True)
    # def lessons(self, request, pk):
    #     l = self.get_object().lesson_set.all()
    #     return Response(LessonSerializer(l, many=True, context={
    #         'request': request
    #     }).data, status=status.HTTP_200_OK)

class ChuyenXeViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = ChuyenXe.objects.all()
    serializer_class = ChuyenXeSerializer
    # permission_classes = [permissions.AllowAny()]

    # def get_permissions(self):
    #     if self.action in ['add_comment', 'like']:
    #         return [permissions.IsAuthenticated()]
    #     return self.permission_classes
    #
    # @action(methods=['post'], url_path="comments", detail=True)
    # def add_comment(self, request, pk):
    #     comment = Comment.objects.create(user=request.user, lesson = self.get_object(), content=request.data.get('content'))
    #     comment.save()
    #
    #     return Response(CommentSerializer(comment, context={
    #         'request': request
    #     }).data, status=status.HTTP_201_CREATED)
    #
    # @action(methods=['post'], url_path='like', detail=True)
    # def like(self, request, pk):
    #     like,create = Like.objects.get_or_create(user=request.user, lesson=self.get_object())
    #     if not create:
    #         like.liked = not like.liked
    #         like.save()
    #
    #     return Response(LessonSerializeDetail(self.get_object(),context={
    #         "request": request
    #     }).data, status=status.HTTP_200_OK)



#account
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    # def get_permissions(self):
    #     if self.action in ['get_current']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]
    #
    # @action(methods=['get'], url_path="current", detail=False)
    # def get_current(self, request):
    #     return Response(UserSerializer(request.user, context={
    #         "request": request
    #     }).data, status=status.HTTP_200_OK)

class TaiXeViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = TaiXe.objects.all()
    serializer_class = TaiXeSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    # def get_permissions(self):
    #     if self.action in ['get_current']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]
    #
    # @action(methods=['get'], url_path="current", detail=False)
    # def get_current(self, request):
    #     return Response(UserSerializer(request.user, context={
    #         "request": request
    #     }).data, status=status.HTTP_200_OK)

class KhachHangViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = KhachHang.objects.all()
    serializer_class = KhachHangSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    # def get_permissions(self):
    #     if self.action in ['get_current']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]
    #
    # @action(methods=['get'], url_path="current", detail=False)
    # def get_current(self, request):
    #     return Response(UserSerializer(request.user, context={
    #         "request": request
    #     }).data, status=status.HTTP_200_OK)

class NhanVienViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = NhanVien.objects.all()
    serializer_class = NhanVienSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    # def get_permissions(self):
    #     if self.action in ['get_current']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]
    #
    # @action(methods=['get'], url_path="current", detail=False)
    # def get_current(self, request):
    #     return Response(UserSerializer(request.user, context={
    #         "request": request
    #     }).data, status=status.HTTP_200_OK)

# Create your views here.
# class CategoryView(View):
#
#     def get(self, request):
#         cats = Category.objects.all()
#         return render(request, 'courses/list.html', {
#             'categories': cats
#         })
#
#     def post(self, request):
#         pass
#
# def index(request):
#     return HttpResponse('HELLO CS2001')
#
# def list(request, course_id):
#     return HttpResponse(f'COURSE {course_id}')



#complain
class ComplainViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    # permission_classes = [perms.OwnerPermission]


