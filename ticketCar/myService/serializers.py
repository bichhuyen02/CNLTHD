from .models import Car, Customer, Category, Complain, Chair, Staff, BStation, PriceT, Trip, Driver, User, Ticket, \
    Invoice
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
        fields = ['id', 'name', 'car', 'active']



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
class BStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BStation
        fields = ['id', 'name', 'description', 'active', 'driver']

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
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'avatar', 'role']

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user

class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ['birth', 'phone', 'user']

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
        fields = ['birth', 'phone', 'user', 'bangLai']

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['birth', 'phone', 'user']



#complain
class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ['id', 'content']