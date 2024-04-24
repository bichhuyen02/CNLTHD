from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response

from . import perms
from .models import Car, Customer, Category, Complain, Chair, Staff, BStation, PriceT, Trip, Driver, User, Invoice, \
    Ticket, Buses
from rest_framework import viewsets, generics, status, permissions, parsers
from .paginator import CoursePaginator, ChairPaginator
# from . import perms
from .serializers import CategorySerializer, CarSerializer, ChairSerializer, PriceTSerializer, BStationSerializer, \
    TripSerializer, UserSerializer, DriverSerializer, CustomerSerializer, StaffSerializer, ComplainSerializer, \
    InvoiceSerializer, TicketSerializer, BusesSerializer




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
    #
    # @action(methods=['get'], detail=True)
    # def car(self, request, pk):
    #     l = self.get_object().car_set.all()
    #     return Response(CarSerializer(l, many=True, context={
    #         'request': request
    #     }).data, status=status.HTTP_200_OK)

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
        chair = self.get_object().chair_set.all()
        return Response(ChairSerializer(chair, many=True, context={
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
            queries = queries.filter(subject__icontains=q)
        return queries

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






# ve
class PriceTViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = PriceT.objects.all()
    serializer_class = PriceTSerializer

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries

class InvoiceViewSet(viewsets.ViewSet,  generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def ticket(self, request, pk):
        ticket = self.get_object().chair_set.all()
        return Response(ChairSerializer(ticket, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class TicketViewSet(viewsets.ViewSet,  generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView,  generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries
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
    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries

    # action(methods=['post'], detail=True)
    # def add_

class BusesViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Buses.objects.all()
    serializer_class = BusesSerializer

    def get_queryset(self):
        queries = self.queryset

        if self.action.__eq__('list'):
            destination = self.request.query_params.get('destination')
            if destination:
                queries = queries.filter(destination=destination)

            departure = self.request.query_params.get('departure')
            if departure:
                queries = queries.filter(departure=departure)

        return queries

class TripViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.AllowAny()]

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            buses = self.request.query_params.get('buses')
            if buses:
                queries = queries.filter(buses=buses)

            dateGo = self.request.query_params.get('dateGo')
            if dateGo:
                queries = queries.filter(dateGo__icontains=dateGo)


        return queries

    def get_permissions(self):
        if self.action in ['add_ticket', 'add_ticket_onl']:
            return [permissions.IsAuthenticated()]
        return self.permission_classes

    @action(methods=['post'], url_path="ticket-onl", detail=True)
    def add_ticket_onl(self, request, pk):
        ticket = Ticket.objects.create(chair= request.data.get('chair'), invoice= request.data.get('invoice'), customer=request.user,
                                       trip=self.get_object())
        ticket.save()

        return Response(TicketSerializer(ticket, context={
            'request': request
        }).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path='ticket', detail=True)
    def ticket(self, request, pk):

        ticket = Ticket.objects.create(chair= request.data.get('chair'), invoice= request.data.get('invoice'),customer= request.user,
                                       trip=self.get_object())
        ticket.save()

        return Response(TicketSerializer(ticket, context={
            'request': request
        }).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path='add_complain', detail=True)
    def add_complain(self, request, pk):
        complain = Complain.objects.create(custumer=request.user, trip=self.get_object(), conten= request.data.get('content'))
        complain.save()

        return Response(TicketSerializer(complain, context={
            'request': request
        }).data, status=status.HTTP_201_CREATED)

    @action(methods=['patch'], url_path='up_complain', detail=True)
    def up_complain(self, request, pk):
        complain = Complain.objects.update(conten=request.data.get('content'))
        complain.save()

        return Response(TicketSerializer(complain, context={
            'request': request
        }).data, status=status.HTTP_202_ACCEPTED)

    @action(methods=['delete'], url_path='de_complain', detail=True)
    def de_complain(self, request, pk):
        complain = Complain.objects.delete(pk)
        complain.save()

        return Response(TicketSerializer(complain, context={
            'request': request
        }).data, status=status.HTTP_201_CREATED)








# account
class UserViewSet(viewsets.ViewSet,  generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView , generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser,  parsers.JSONParser]

    def get_permissions(self):
        if self.action in ['current_user']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries

    @action(methods=['get'], url_path="current-user", detail=False)
    def current_user(self, request):
        return Response(UserSerializer(request.user, context={
            "request": request
        }).data, status=status.HTTP_200_OK)

class DriverViewSet(viewsets.ViewSet,  generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries
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

class CustomerViewSet(viewsets.ViewSet,  generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries
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

class StaffViewSet(viewsets.ViewSet,  generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.JSONParser]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries

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







# complain
class ComplainViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [perms.OwnerPermission]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries
