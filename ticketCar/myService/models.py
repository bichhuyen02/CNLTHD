from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField



role_user = ['Customer', 'Staff', 'Driver', 'Admin']
role_choices = sorted([(item, item) for item in role_user])

role_date = ['Lễ_Ghế', 'Lễ_Giường', 'Thường_Ghế', 'Thường_Giường']
role_date = sorted([(item, item) for item in role_date])

#account
class User(AbstractUser):
    phone = models.CharField(max_length=10, null=True, unique=True)
    avatar = models.ImageField(upload_to="ava/%Y/%m", null=True)
    role = models.CharField(choices=role_choices, max_length=20, default="Customer")

class Staff(models.Model):
    birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Driver(models.Model):
    birth = models.DateField()
    license = models.ImageField(upload_to="license/%Y/%m", null=True)
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
    price = models.FloatField( blank=True)
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
    image = models.ImageField(upload_to="xe/%Y/%m", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Biển số: {}, Loại: {}".format(self.licensePlates, self.category.name)

class Chair(BaseModel):
    name = models.CharField(max_length=50, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'car')




#chuyến xe
class Province(BaseModel):
    name = models.CharField(max_length=100)
    description = RichTextField(null=True)
    def __str__(self):
        return self.name

class BStation(BaseModel):
    name = models.CharField(max_length=50, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'province')

class Buses(BaseModel):
    destination = models.ForeignKey(BStation, related_name='trip_destination', on_delete=models.CASCADE, blank=True)
    departure = models.ForeignKey(BStation, related_name='trip_departure', on_delete=models.CASCADE, blank=True)

    class Meta:
        unique_together = ('destination', 'departure')

    def __str__(self):
        return "Đi: {}, Đến: {}".format(self.departure.name, self.destination.name)

class Bus_BSta(BaseModel):
    buses = models.ForeignKey(Buses, on_delete=models.CASCADE)
    bStation = models.ForeignKey(BStation, on_delete=models.CASCADE)
    def __str__(self):
        return "Chuyến: {}, Bến: {}".format(self.buses, self.bSatation.name)

class Trip(BaseModel):
    timeGo = models.TimeField(blank=True)
    dateGo = models.DateField(blank=True)
    description = RichTextField(blank=False)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    buses = models.ForeignKey(Buses, on_delete=models.CASCADE)
    price = models.ForeignKey(PriceT, on_delete=models.CASCADE)






#vé
class Invoice(BaseModel):
    amout = models.FloatField(blank=False)
    def __str__(self):
        return str(self.amout)

class Ticket(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,default=1)
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return self.chair.name




#complain
class Complain(BaseModel):
    content = models.CharField(max_length=255, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.content