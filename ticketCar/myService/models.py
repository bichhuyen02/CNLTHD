from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField




class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=True)
    active = models.BooleanField(default=True)


class NhanVien(models.Model):
    phone = models.CharField(max_length=10)
    birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class KhachHang(models.Model):
    phone = models.CharField(max_length=10)
    birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class TaiXe(models.Model):
    phone = models.CharField(max_length=10)
    birth = models.DateField()
    bangLai = CloudinaryField('bang', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class LoaiXe(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Xe(BaseModel):
    name = models.CharField(max_length=100)
    bienSo = models.CharField(max_length=20)
    image = models.ImageField(upload_to="xe/%Y/%m")
    loaiXe = models.ForeignKey(LoaiXe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'loaiXe')


class Ghe(BaseModel):
    name = models.CharField(max_length=50)
    description = RichTextField(null=True)
    xe = models.ForeignKey(Xe, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'xe')

class BenXe(BaseModel):
    name = models.CharField(max_length=50)
    description = RichTextField(null=True)
    def __str__(self):
        return self.name


# class BenXeDi(BaseModel):
#     name = models.CharField(max_length=50)
#     description = RichTextField(null=True)
#     def __str__(self):
#         return self.name


class ChuyenXe(BaseModel):
    gioXP = models.TimeField()
    ngayXP = models.DateField()
    description = RichTextField(null=True)
    diemDen = models.ForeignKey(BenXe, related_name='chuyenxe_diemden', on_delete=models.CASCADE)
    diemDi = models.ForeignKey(BenXe, related_name='chuyenxe_diemdi', on_delete=models.CASCADE)



class Complain(BaseModel):
    content = models.CharField(max_length=255)
    chuyenXe = models.ForeignKey(ChuyenXe, on_delete=models.CASCADE)
    khachHang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)


class GiaVe(BaseModel):
    gia = models.IntegerField()
    loai = models.CharField(max_length=20)
    def __str__(self):
        return self.gia