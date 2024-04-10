from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField



role_user = ['Customer', 'Staff', 'Driver']
role_choices = sorted([(item, item) for item in role_user])

#account
class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=True)
    active = models.BooleanField(default=True)
    role = models.CharField(max_length= 20, choices=role_choices, default='Customer')

class Staff(models.Model):
    phone = models.CharField(max_length=10, null=True)
    birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Customer(models.Model):
    phone = models.CharField(max_length=10, null=True)
    birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Driver(models.Model):
    phone = models.CharField(max_length=10, null=True)
    birth = models.DateField()
    license = CloudinaryField('license', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']




#xe
class Category(BaseModel):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Car(BaseModel):
    licensePlates = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to="xe/%Y/%m", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.licensePlates

    class Meta:
        unique_together = ('licensePlates', 'category')

class Chair(BaseModel):
    name = models.CharField(max_length=50, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'car')




#chuyến xe
class BStation(BaseModel):
    name = models.CharField(max_length=50, null=True)
    description = RichTextField()
    def __str__(self):
        return self.name

class Trip(BaseModel):
    timeGo = models.TimeField(null=True)
    dateGo = models.DateField(null=True)
    description = RichTextField()
    destination = models.ForeignKey(BStation, related_name='trip_destination', on_delete=models.CASCADE, null=True)
    departure = models.ForeignKey(BStation, related_name='trip_departure', on_delete=models.CASCADE, null=True)





#giá vé
class PriceT(BaseModel):
    price = models.FloatField(null=True)
    date_cate = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.price




#complain
class Complain(BaseModel):
    content = models.CharField(max_length=255, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.content