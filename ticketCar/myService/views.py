from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response

from . import perms
from .models import Car, Customer, Category, Complain, Chair, Staff, BStation, PriceT, Trip, Driver, User, Invoice, \
    Ticket, Buses, Province, Bus_BSta
from rest_framework import viewsets, generics, status, permissions, parsers
from .paginator import CoursePaginator, ChairPaginator
from . import perms
from .serializers import CategorySerializer, CarSerializer, ChairSerializer, PriceTSerializer, BStationSerializer, \
    TripSerializer, UserSerializer, DriverSerializer, CustomerSerializer, StaffSerializer, ComplainSerializer, \
    InvoiceSerializer, TicketSerializer, BusesSerializer, ProvinceSerializer, Bus_BStaSerializer




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

class CarViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

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





# ve
class PriceTViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = PriceT.objects.all()
    serializer_class = PriceTSerializer

class InvoiceViewSet(viewsets.ViewSet,  generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    @action(methods=['get'], detail=True)
    def ticket(self, request, pk):
        ticket = self.get_object().chair_set.all()
        return Response(ChairSerializer(ticket, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class TicketViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.ListAPIView,  generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            chair = self.request.query_params.get('chair')
            if chair:
                queries = queries.filter(chair=chair)

            trip = self.request.query_params.get('trip')
            if trip:
                queries = queries.filter(trip=trip)

        return queries






# chuyen xe
class ProvinceViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    @action(methods=['get'], detail=True)
    def bStation(self, request, pk):
        l = self.get_object().bStation_set.all()
        return Response(BStationSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class BStationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = BStation.objects.all()
    serializer_class = BStationSerializer

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            name = self.request.query_params.get('name')
            if name:
                queries = queries.filter(name=name)

            province = self.request.query_params.get('province')
            if province:
                queries = queries.filter(province=province)

        return queries

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

class Bus_BStaViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Bus_BSta.objects.all()
    serializer_class = Bus_BStaSerializer

    def get_queryset(self):
        queries = self.queryset

        if self.action.__eq__('list'):
            buses = self.request.query_params.get('buses')
            if buses:
                queries = queries.filter(buses=buses)

            bStation = self.request.query_params.get('bStation')
            if bStation:
                queries = queries.filter(bStation=bStation)

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
        chair = Chair.objects.get(id=request.data.get('chair'))
        invoice = Invoice.objects.get(id=request.data.get('invoice'))
        customer = Customer.objects.get(id=request.user.id)
        ticket = Ticket.objects.create(chair= chair, invoice= invoice, customer=customer,
                                       trip=self.get_object())
        ticket.save()

        return Response(TicketSerializer(ticket, context={
            'request': request
        }).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path='ticket', detail=True)
    def ticket(self, request, pk):
        chair = Chair.objects.get(id=request.data.get('chair'))
        invoice = Invoice.objects.get(id=1)
        phones = request.data.get('phone')
        user = Customer.get_or_create(phone=phones.strip())
        ticket = Ticket.objects.create(chair=chair, invoice=invoice, staff=request.user,
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

    @action(methods=['get'], detail=True)
    def info(self, request):
        l = self.get_object().all
        if l.role.__eq__('Customer'):
            l = self.get_object().customer_set.all()
            return Response(CustomerSerializer(l, many=True, context={
                'request': request
            }).data, status=status.HTTP_200_OK)
        else:
            if l.role.__eq__('Staff'):
                l = self.get_object().staff_set.all()
                return Response(StaffSerializer(l, many=True, context={
                    'request': request
                }).data, status=status.HTTP_200_OK)
            else:
                if l.role.__eq__('driver'):
                    l = self.get_object().driver_set.all()
                    return Response(DriverSerializer(l, many=True, context={
                        'request': request
                    }).data, status=status.HTTP_200_OK)

class DriverViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permissions = [permissions.AllowAny()]

    def get_permissions(self):
        if self.action in ['trip']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=True)
    def trip(self, request):
        l = self.get_object().trip_set.filter(active=True).all()
        return Response(TripSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class CustomerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny()]

    def get_queryset(self):
        queries = self.queryset
        phone = self.request.query_params.get('phone')
        if phone:
            queries = queries.filter(phone=phone)

        return queries

    def get_permissions(self):
        if self.action in ['ticket']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=True)
    def ticket(self, request):
        l = self.get_object().ticket_set.all()
        return Response(TicketSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class StaffViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.AllowAny()]

    def get_permissions(self):
        if self.action in ['ticket']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], detail=True)
    def ticket(self, request):
        l = self.get_object().ticket_set.all()
        return Response(TicketSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)






# complain
class ComplainViewSet(viewsets.ViewSet, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [perms.OwnerPermission]

