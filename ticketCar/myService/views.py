from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car, Customer, Category, Complain, Chair, Staff, BStation, PriceT, Trip, Driver,User
from rest_framework import viewsets, generics, status, permissions, parsers
from .paginator import CoursePaginator, ChairPaginator
# from . import perms
from .serializers import CategorySerializer, CarSerializer, ChairSerializer, PriceTSerializer, BStationSerializer, \
    TripSerializer, UserSerializer, DriverSerializer, CustomerSerializer, StaffSerializer, ComplainSerializer




# xe
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def xe(self, request, pk):
        l = self.get_object().car_set.all()
        return Response(CarSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class CarViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # pagination_class = CoursePaginator
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(licensePlates__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def chair(self, request, pk):
        l = self.get_object().chair_set.all()
        return Response(ChairSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class ChairViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer
    # permission_classes = [permissions.AllowAny()]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    # def get_permissions(self):
    #     if self.action in ['add_comment', 'like']:
    #         return [permissions.IsAuthenticated()]
    #     return self.permission_classes
    #
    # @action(methods=['patch'], detail=True)
    # def update_active(self, request, pk):
    #     chair = Chair.objects.update(active=False)
    #     chair.save()
    #
    #     return Response(ChairSerializer(chair, context={
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




# ve
class PriceTViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = PriceT.objects.all()
    serializer_class = PriceTSerializer

class TicketViewSet(viewsets.ViewSet, generics.ListAPIView):
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




# chuyen xe
class BStationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = BStation.objects.all()
    serializer_class = BStationSerializer
    # pagination_class = CoursePaginator
    # permission_classes = [permissions.IsAuthenticated]

class TripViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
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




# account
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

class DriverViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
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

class CustomerViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
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

class StaffViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
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


# complain
class ComplainViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    # permission_classes = [perms.OwnerPermission]
