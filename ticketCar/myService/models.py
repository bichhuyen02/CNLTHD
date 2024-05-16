import uuid
from lib2to3.pgen2 import driver

from django.core.files.storage import storages
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from datetime import date



current_date = date.today()

role_user = ['Customer', 'Staff', 'Driver', 'Admin']
role_choices = sorted([(item, item) for item in role_user])

role_dates = ['Lễ', 'Thường']
role_date = sorted([(item, item) for item in role_dates])

role_sls = ['16', '25', '50']
role_sl = sorted([(item, item) for item in role_sls])



#account
class User(AbstractUser):
    phone = models.CharField(max_length=10, null=True, unique=True)
    avatar = models.CharField(max_length=255, blank=True)
    role = models.CharField(choices=role_choices, max_length=20, default="Customer")
class Staff(models.Model):
    birth = models.DateField(default=current_date)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Customer(models.Model):
    birth = models.DateField(default=current_date)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
class Driver(models.Model):
    birth = models.DateField(default=current_date)
    license = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username




class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']



#giá
class PriceT(BaseModel):
    price = models.FloatField(blank=True)
    date_cate = models.CharField(choices=role_date, max_length=50, blank=True, default="Lễ_Ghế")

    def __str__(self):
        return "loại: {}, giá: {}".format(self.date_cate, str(self.price))







#xe
class Category(BaseModel):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Car(BaseModel):
    licensePlates = models.CharField(max_length=20, null=True)
    image = models.CharField(max_length=255, blank=True)
    quantity = models.CharField(choices=role_sl, max_length=5, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Biển số: {}, Loại: {}".format(self.licensePlates, self.category)





#chuyến xe
class Province(BaseModel):
    name = models.CharField(max_length=100)
    description = RichTextField(null=True)
    def __str__(self):
        return self.name

class BStation(BaseModel):
    name = models.CharField(max_length=50, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    description = RichTextField(null=True)
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'province')
class Bues(BaseModel):
    destination = models.ForeignKey(Province, related_name='trip_destination', on_delete=models.CASCADE, blank=True) #đến
    departure = models.ForeignKey(Province, related_name='trip_departure', on_delete=models.CASCADE, blank=True) #đi
    description = RichTextField(blank=False)

    def __str__(self):
        return "đi: {}, đến: {}".format(self.departure, self.destination)
class Trip(BaseModel):
    quantity = models.IntegerField()
    timeGo = models.TimeField(blank=True)
    dateGo = models.DateField(blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    bues = models.ForeignKey(Bues, on_delete=models.CASCADE)
    def __str__(self):
        return "xe: {}, chuyến: {}".format(self.car, self.bues)
class TripCar(BaseModel):
    pointGo = models.ForeignKey(BStation, related_name='tripCar_go', on_delete=models.CASCADE)
    pointUp = models.ForeignKey(BStation, related_name='tripCar_up', on_delete=models.CASCADE)
    price = models.ForeignKey(PriceT, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)




#vé
class Invoice(BaseModel):
    amout = models.FloatField(blank=False)
    def __str__(self):
        return str(self.amout)
class Ticket(BaseModel):
    quantity = models.IntegerField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,default=1)
    trip = models.ForeignKey(TripCar, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.user.username




#complain
class Complain(BaseModel):
    content = models.CharField(max_length=255, blank=True)
    trip = models.ForeignKey(TripCar, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.content