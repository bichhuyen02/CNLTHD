from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car, Customer, Category, Complain, Staff, BStation, PriceT, Trip, Driver, User, Invoice, \
    Ticket, Province, Bues, TripCar
from rest_framework import viewsets, generics, status, permissions, parsers
from .paginator import CoursePaginator, ChairPaginator
from . import perms
from .serializers import CategorySerializer, CarSerializer, PriceTSerializer, BStationSerializer, \
    TripSerializer, UserSerializer, DriverSerializer, CustomerSerializer, StaffSerializer, ComplainSerializer, \
    InvoiceSerializer, TicketSerializer, ProvinceSerializer, BuesSerializer, TripCarSerializer
from django.core.files.storage import default_storage
from .firebase import storage



# xe
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
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






# ve
class PriceTViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = PriceT.objects.all()
    serializer_class = PriceTSerializer

class InvoiceViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class TicketViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.ListAPIView,  generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            customer = self.request.query_params.get('customer')
            c = Customer.objects.get(id=customer)
            if c:
                queries = queries.filter(customer=c)

            staff = self.request.query_params.get('staff')
            if staff:
                queries = queries.filter(staff=staff)

            trip = self.request.query_params.get('trip')
            if trip:
                queries = queries.filter(trip=trip)

        return queries





# chuyen xe
class ProvinceViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    @action(methods=['get'], detail=True)
    def bStation(self, request, pk):
        l = self.get_object().bStation_set.all()
        return Response(BStationSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

class BStationViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
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

            active = True
            if active:
                queries = queries.filter(active=active)
        return queries
class BuesViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Bues.objects.all()
    serializer_class = BuesSerializer

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            destination = self.request.query_params.get('destination')#đến
            if id:
                queries = queries.filter(destination=destination)

            departure = self.request.query_params.get('departure')  # đi
            if id:
                queries = queries.filter(departure=departure)

            name = self.request.query_params.get('name')
            if name:
                queries = queries.filter(name=name)

            province = self.request.query_params.get('province')
            if province:
                queries = queries.filter(province=province)

            active = True
            if active:
                queries = queries.filter(active=active)
        return queries

class TripViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            buses = self.request.query_params.get('buses')
            if buses:
                queries = queries.filter(buses=buses)

            dateGo = self.request.query_params.get('dateGo')
            if dateGo:
                queries = queries.filter(dateGo__icontains=dateGo)

            active = True
            if active:
                queries = queries.filter(active=active)
        return queries

class TripCarViewSet(viewsets.ViewSet, generics.ListAPIView,generics.RetrieveAPIView):
        queryset = TripCar.objects.all()
        serializer_class = TripCarSerializer

        def get_queryset(self):
            queries = self.queryset
            if self.action.__eq__('list'):
                trip = self.request.query_params.get('trip')
                if trip:
                    queries = queries.filter(trip=trip)
                active = True
                if active:
                    queries = queries.filter(active=active)
            return queries

        def get_permissions(self):
            if self.action in ['add_ticket', 'add_ticket_onl']:
                return [permissions.IsAuthenticated()]
            return self.permission_classes

        @action(methods=['post'], url_path="ticket-onl", detail=True)
        def add_ticket_onl(self, request, pk):
            invoice = Invoice.objects.get(id=request.data.get('invoice'))
            customer = Customer.objects.get(id=request.user.id)
            ticket = Ticket.objects.create(invoice=invoice, customer=customer, quantity=request.data.get('quantity'),
                                           trip=self.get_object(), active=request.data.get('active'))

            # price = float(self.get_object().price.price)
            # quantity = float(request.data.get('quantity'))
            # invoice.amout = price * quantity
            #
            # self.get_object().trip.quantity = self.get_object().trip.quantity - quantity

            ticket.save()
            # invoice.save()
            # self.get_object().save()

            return Response(TicketSerializer(ticket, context={
                'request': request
            }).data, status=status.HTTP_201_CREATED)

        @action(methods=['post'], url_path='ticket', detail=True)
        def ticket(self, request, pk):
            invoice = Invoice.objects.get(id=1)
            phones = request.data.get('phone')
            user = Customer.get_or_create(phone=phones.strip())
            ticket = Ticket.objects.create(invoice=invoice, staff=request.user, customer=user, quantity=request.data.get('quantity'),
                                           trip=self.get_object(), active=request.data.get('active'))

            # price = float(self.get_object().price.price)
            # quantity = float(request.data.get('quantity'))
            # invoice.amout = price * quantity
            #
            # self.get_object().trip.quantity = self.get_object().trip.quantity - quantity

            ticket.save()
            # invoice.save()
            # self.get_object().save()

            return Response(TicketSerializer(ticket, context={
                'request': request
            }).data, status=status.HTTP_201_CREATED)

        @action(methods=['post'], url_path='add_complain', detail=True)
        def add_complain(self, request, pk):
            customer = Customer.objects.get(id=request.user.id)
            complain = Complain.objects.create(custumer=customer, trip=self.get_object(),
                                               conten=request.data.get('content'))
            complain.save()

            return Response(TicketSerializer(complain, context={
                'request': request
            }).data, status=status.HTTP_201_CREATED)








# account
class UserViewSet(viewsets.ViewSet, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView , generics.RetrieveAPIView):
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

    @action(methods=['post'], detail=True)
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

    @action(methods=['post'], detail=False)
    def user(self, request):
        image = request.data.get('avatar')
        if image:
            # Convert the InMemoryUploadedFile to string
            filename = image.name

            # Upload the image to Firebase Storage
            file_path = default_storage.save('tmp/' + filename, image)
            with default_storage.open(file_path, 'rb') as file:
                storage.child("ava/" + filename).put(file)

            download_url = storage.child("ava/" + filename).get_url(None)
            print(download_url)
            image = download_url
            user = User.objects.create(avatar=download_url, username=request.data.get('username'), password=request.data.get('password'),
            first_name=request.data.get('first_name'), last_name=request.data.get('last_name'), email=request.data.get('email'), phone=request.data.get('phone'))
            user.save()
            Customer.objects.create(user=user)
            return Response(UserSerializer(user, context={'request': request}).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
        if self.action.__eq__('list'):
            user = self.request.query_params.get('user')
            if user:
                queries = queries.filter(user=user)
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
class ComplainViewSet(viewsets.ViewSet, generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [perms.OwnerPermission]

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            trip = self.request.query_params.get('trip')
            if trip:
                queries = queries.filter(trip=trip)
            user = self.request.query_params.get('customer')
            c = Customer.objects.get(id=user)
            if c:
                queries = queries.filter(customer=c)
        return queries

