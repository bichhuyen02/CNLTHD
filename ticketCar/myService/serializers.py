from .models import Car, Customer, Category, Complain, Chair, Staff, BStation, PriceT, Trip, Driver, User, Ticket, \
    Invoice, Buses, Province, Bus_BSta
from rest_framework import serializers




#xe
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'active']

class CarSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    # loaiXe = LoaiXeSerializer()

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.image.name)
            return "/static/%s" % obj.image.name


    class Meta:
        model = Car
        fields = ['id', 'licensePlates', 'category', 'image', 'active']

class ChairSerializer(serializers.ModelSerializer):
    # xe = XeSerializer()
    class Meta:
        model = Chair
        fields = '__all__'



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
        fields = ['id', 'staff', 'customer', 'chair', 'active', 'created_date', 'updated_date', 'invoice']




#chuyen xe
class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ['id', 'name', 'active']

class BStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BStation
        fields = ['id', 'name', 'active', 'province']

class BusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buses
        fields = ['id', 'destination', 'departure', 'active']

class Bus_BStaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus_BSta
        fields = ['id', 'buses', 'active', 'bStation']

class TripSerializer(serializers.ModelSerializer):
    # diemDen = TagSerializer(many=True)
    class Meta:
        model = Trip
        fields = '__all__'



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
    bangLai = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.bangLai:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.bangLai.name)
            return "/static/%s" % obj.bangLai.name


    class Meta:
        model = Driver
        fields = ['birth', 'user', 'bangLai']

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['birth', 'user']



#complain
class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ['id', 'content']