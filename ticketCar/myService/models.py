from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


# Create your models here.
class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']

class nhanvien(User):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    birth = models.DateField()

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="courses/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')


class Lesson(BaseModel):
    subject = models.CharField(max_length=50)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="lessons/%Y/%m")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Interaction(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Comment(Interaction):
    content = models.CharField(max_length=255)

class Like(Interaction):
    active_like = models.BooleanField()

class Rating(Interaction):
    rate = models.SmallIntegerField(default=0)