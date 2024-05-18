from .models import Car, Customer, Category, Complain, Staff, BStation, PriceT, Trip, Driver, User, Ticket, \
    Invoice, Province, Bues, TripCar
from rest_framework import serializers




#xe
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'active']
class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'licensePlates', 'category', 'image', 'active', 'quantity']




#ve
class PriceTSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceT
        fields = ['id', 'price', 'date_cate', 'active']
class InvoiceSerializer(serializers.ModelSerializer):
     class Meta:
         model = Invoice
         fields = '__all__'
class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['id', 'staff', 'customer', 'active', 'created_date', 'updated_date', 'invoice', 'quantity']




#chuyen xe
class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ['id', 'name', 'active']
class BStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BStation
        fields = ['id', 'name', 'active', 'province']
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
class TripCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripCar
        fields = '__all__'
class BuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bues
        fields = ['id', 'destination', 'active', 'departure']




#account
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        model = User
        fields = ['last_name', 'username', 'password', 'avatar', 'role', 'phone']

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user
class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ['birth', 'user']
class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ['birth', 'user', 'license']
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['birth', 'user']



#complain
class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ['id', 'content']