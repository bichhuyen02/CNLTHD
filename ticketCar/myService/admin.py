import uuid

from admin_interface.models import Theme
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.conf import settings
from django.contrib import admin, messages
from django import forms
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.utils.safestring import mark_safe
from .models import Car, Customer, Category, Staff, BStation, PriceT, Trip, Driver, User, Province, Bues, TripCar
from .firebase import storage
from datetime import date
from django.core.mail import send_mail





class MyServiceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        # Lấy thông tin người dùng đăng nhập
        user = request.user
        print(user.role)
        # Kiểm tra quyền truy cập của người dùng
        if user.role.__eq__('Admin'):
            # Người dùng là superuser, không áp dụng exclude
            return {'add': True, 'change': True, 'delete': True}
        else:
            # Người dùng không phải là superuser, áp dụng exclude
            return {'add': False, 'change': False, 'delete': False}

    def get_readonly_fields(self, request, obj=None):
        if request.user.role == 'Admin':
            return super(MyServiceAdmin, self).get_readonly_fields(request, obj)
        else:
            exclude = ('model1', 'model2')
            return [f.name for f in self.model._meta.fields]



#my admin
class AppAdminSite(admin.AdminSite):
    site_title = 'SellTicket'
    site_header = 'HỆ THỐNG BÁN VÉ XE TRỰC TUYẾN'
    index_title = 'QUẢN LÝ BÁN VÉ XE TRỰC TUYẾN'

    # def get_urls(self):
    #     return [
    #                path('course-stats/', self.stats_view)
    #            ] + super().get_urls()
    #
    # def stats_view(self, request):
    #     stats = count_course_by_cat()
    #     return TemplateResponse(request, 'admin/stats_view.html',context={
    #         'stats': stats
    #     })





#form
class TripForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget, required=False)
    class Meta:
        model = Trip
        fields = '__all__'
class BStationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget, required=False)

    class Meta:
        model = BStation
        fields = '__all__'
class ProvinceForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget, required=False)

    class Meta:
        model = Province
        fields = '__all__'
class BuesForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget, required=False)

    class Meta:
        model = Bues
        fields = '__all__'



# xe
class CategoryAdmin(MyServiceAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)
class CarAdmin(MyServiceAdmin):
    list_display = ['id', 'licensePlates', 'category', 'active']
    search_fields = ['id', 'licensePlates', 'active']
    list_filter = ['id', 'licensePlates']
    # inlines = [XeTagInlineAdmin]
    readonly_fields = ['img']

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'image':
            # Thêm trường tùy chỉnh để upload hình ảnh
            kwargs['widget'] = forms.ClearableFileInput(attrs={'accept': 'image/*'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        try:
            image = request.FILES.get('image')
            obj.save()

            if image:
                # Convert the InMemoryUploadedFile to string
                filename = image.name

                # Upload the image to Firebase Storage
                file_path = default_storage.save('tmp/' + filename, image)
                with default_storage.open(file_path, 'rb') as file:
                    storage.child("img/" + filename).put(file)

                download_url = storage.child("img/" + filename).get_url(None)

                # Assign the download URL to your model field
                obj.image = download_url
                obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)

    def img(self, obj):
        if obj:
            return mark_safe(
                '<img src="{url}" width="120" />'.format(url=obj.image)
            )




# chuyen xe
class ProvinceAdmin(MyServiceAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']
    form = ProvinceForm

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)
class BStationAdmin(MyServiceAdmin):
    list_display = ['id', 'name', 'province']
    search_fields = ['name']
    list_filter = ['id', 'name']
    form = BStationForm

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)
class BuesAdmin(MyServiceAdmin):
    list_display = ['destination', 'departure']
    search_fields = ['destination', 'departure']
    list_filter = ['destination', 'departure']
    form = BuesForm

    def save_model(self, request, obj, form, change):
        pointGo = request.POST.get('destination')
        pointUp = request.POST.get('departure')
        if pointGo != pointUp:
            obj.save()
        else:
            raise ValidationError("Lỗi: 2 điểm đi và đến không được trùng nhau.")
class TripAdmin(MyServiceAdmin):
    list_display = ['car', 'bues', 'timeGo', 'dateGo', 'driver']
    search_fields = ['car', 'timeGo', 'dateGo', 'driver']
    list_filter = ['car', 'timeGo', 'dateGo', 'driver']

    def save_model(self, request, obj, form, change):
        date1 = form.cleaned_data.get('dateGo')
        current_date = date.today()
        # queries = Trip.queryset

        delta = date1 - current_date
        print(date1)
        if delta.days >= 2:
            tripD = Trip.objects.filter(dateGo=date1, driver=request.POST.get('driver')).exists()
            tripC = Trip.objects.filter(dateGo=date1, car=request.POST.get('car')).exists()
            print(tripC)
            # Thêm điều kiện kiểm tra trước khi lưu đối tượng
            if not tripD:
                if not tripC:
                    obj.save()
                else:
                    raise ValidationError("Lỗi: Xe đã có chuyến trong ngày hôm đó.")
            else:
                raise ValidationError("Lỗi: Tài xế đã có chuyến trong ngày hôm đó.")
        else:
            raise ValidationError("Lỗi: Thời gian chạy không hợp lệ.")
class TripCarAdmin(MyServiceAdmin):
    list_display = ['id', 'pointGo', 'price', 'pointUp']
    search_fields = ['pointUp', 'pointGo']
    list_filter = ['pointUp', 'pointGo']

    def save_model(self, request, obj, form, change):
            pointGo = request.POST.get('pointGo')
            pointUp = request.POST.get('pointUp')
            if pointGo != pointUp:
                obj.save()
            else:
                raise ValidationError("Lỗi: 2 điểm đi và đến không được trùng nhau")





# account
class UserAdmin(MyServiceAdmin):
    list_display = ['id', 'username', 'last_name', 'role']
    search_fields = ['username', 'role']
    list_filter = ['username', 'role']
    readonly_fields = ['ava']

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'avatar':
            # Thêm trường tùy chỉnh để upload hình ảnh
            kwargs['widget'] = forms.ClearableFileInput(attrs={'accept': 'image/*'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        try:
            role = request.POST.get('role')
            image = request.FILES.get('avatar')
            obj.save()
            if image:
                # Convert the InMemoryUploadedFile to string
                filename = image.name

                # Upload the image to Firebase Storage
                file_path = default_storage.save('tmp/' + filename, image)
                with default_storage.open(file_path, 'rb') as file:
                    storage.child("ava/" + filename).put(file)

                download_url = storage.child("ava/" + filename).get_url(None)
                print(download_url)
                # Assign the download URL to your model field
                obj.avatar = download_url
                obj.save()
                subject = 'welcome to GFG world'
                message = f'Hi huyen, thank you for registering in geeksforgeeks.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['tsanthibichhuyen200@gmail.com', ]
                send_mail(subject, message, email_from, recipient_list)


            if role.__eq__('Customer'):
                c = Customer.objects.create(user=obj)
                c.save()
            else:
                if role.__eq__('Staff'):
                    obj.is_superuser = True
                    obj.is_staff = True
                    obj.save()
                    s = Staff.objects.create(user=obj)
                    s.save()
                else:
                    if role.__eq__('Driver'):
                        d = Driver.objects.create(user=obj)
                        d.save()
                    else:
                        if role.__eq__('Admin'):
                            obj.is_superuser = True
                            obj.is_staff = True
                            obj.save()
        except Exception as e:
             self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)



    def ava(self, obj):
        if obj:
            return mark_safe(
                '<img src="{url}" width="120" />'.format(url=obj.avatar)
            )
class CustomerAdmin(MyServiceAdmin):
    list_display = ['id', 'user']
    search_fields = ['user']
    list_filter = ['user']
    readonly_fields = ['user']

    def has_add_permission(self, request):
        return False
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)
class StaffAdmin(MyServiceAdmin):
    list_display = ['id', 'user']
    search_fields = ['user']
    list_filter = ['user']
    readonly_fields = ['user']

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)
class DriverAdmin(MyServiceAdmin):
    list_display = ['id', 'user']
    search_fields = ['user']
    list_filter = ['user']
    readonly_fields = ['licen', 'user']

    def has_add_permission(self, request):
        return False

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'license':
            # Thêm trường tùy chỉnh để upload hình ảnh
            kwargs['widget'] = forms.ClearableFileInput(attrs={'accept': 'image/*'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        try:
            image = request.FILES.get('license')
            obj.save()

            if image:
                # Convert the InMemoryUploadedFile to string
                filename = image.name

                # Upload the image to Firebase Storage
                file_path = default_storage.save('tmp/' + filename, image)
                with default_storage.open(file_path, 'rb') as file:
                    storage.child("licen/" + filename).put(file)

                download_url = storage.child("licen/" + filename).get_url(None)
                print(download_url)
                # Assign the download URL to your model field
                obj.license = download_url
                obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)

    def licen(self, obj):
        if obj:
            return mark_safe(
                '<img src="{url}" width="120" />'.format(url=obj.license)
            )





# gia ve
class PriceTAdmin(MyServiceAdmin):
    list_display = ['id', 'price', 'date_cate']
    search_fields = ['price', 'date_cate']
    list_filter = ['price', 'date_cate']

    # formfield_overrides = {
    #     PriceT.price: {'widget': admin.widgets.AdminTextInputWidget(attrs={'type': 'number'})},}

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except Exception as e:
            self.message_user(request, f"Lỗi: {str(e)}", messages.ERROR)


admin_site = AppAdminSite(name='Quản lý bán vé')

admin_site.register(Car, CarAdmin)
admin_site.register(Category, CategoryAdmin)


admin_site.register(Province, ProvinceAdmin)
admin_site.register(BStation, BStationAdmin)
admin_site.register(Bues, BuesAdmin)
admin_site.register(TripCar, TripCarAdmin)
admin_site.register(Trip, TripAdmin)


admin_site.register(PriceT, PriceTAdmin)


admin_site.register(Staff, StaffAdmin)
admin_site.register(Customer, CustomerAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Driver, DriverAdmin)

admin_site.register(Theme, MyServiceAdmin)




