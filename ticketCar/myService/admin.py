from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Car, Customer, Category, Complain, Chair, Staff, BStation, PriceT, Trip, Driver, User, Ticket, \
    Invoice, Buses, Province, Bus_BSta


# Register your models here.

class MyServiceAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if request.user.role == 'Admin':
            return super(MyServiceAdmin, self).get_readonly_fields(request, obj)
        else:
            return [f.name for f in self.model._meta.fields]


class AppAdminSite(admin.AdminSite):
    site_header = 'HỆ THỐNG BÁN VÉ XE TRỰC TUYẾN'

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


# class XeTagInlineAdmin(admin.TabularInline):
#     model = Xe.tags.through
#
# class LessonTagInlineAdmin(admin.TabularInline):
#     model = Lesson.tags.through

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


# xe
class CategoryAdmin(MyServiceAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CarAdmin(MyServiceAdmin):
    list_display = ['id', 'licensePlates', 'category', 'active']
    search_fields = ['id', 'licensePlates', 'active']
    list_filter = ['id', 'licensePlates']
    # form = CourseForm
    # inlines = [XeTagInlineAdmin]
    readonly_fields = ['ava']

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    def ava(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


class ChairAdmin(MyServiceAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


# chuyen xe
class ProvinceAdmin(MyServiceAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']
    form = BStationForm


class BStationAdmin(MyServiceAdmin):
    list_display = ['id', 'name', 'province']
    search_fields = ['name']
    list_filter = ['id', 'name']
    form = BStationForm


class BusesAdmin(MyServiceAdmin):
    list_display = ['id', 'destination', 'departure']
    search_fields = ['id']
    list_filter = ['id']


class Bus_BStaAdmin(MyServiceAdmin):
    list_display = ['id', 'buses', 'bStation']
    search_fields = ['id']
    list_filter = ['id']


class TripAdmin(MyServiceAdmin):
    list_display = ['id', 'timeGo', 'dateGo', 'price']
    search_fields = ['timeGo', 'dateGo']
    list_filter = ['timeGo', 'dateGo']
    form = TripForm

    # def save_model(self, request, obj, form, change):
    #     # Thêm điều kiện kiểm tra trước khi lưu đối tượng
    #     trip = Trip.object.filter(active=True, driver=request.data.get('driver'))
    #
    #     # if trip. != trip.:
    #     #     # Lưu đối tượng vào cơ sở dữ liệu
    #     #     obj.save()


# account
class UserAdmin(MyServiceAdmin):
    list_display = ['id', 'username', 'last_name', 'role', 'phone']
    search_fields = ['username', 'role']
    list_filter = ['username', 'role']


class CustomerAdmin(MyServiceAdmin):
    list_display = ['id', 'user']
    search_fields = ['user']
    list_filter = ['user']


class StaffAdmin(MyServiceAdmin):
    list_display = ['id', 'user']
    search_fields = ['user']
    list_filter = ['user']


class DriverAdmin(MyServiceAdmin):
    list_display = ['id', 'user']
    search_fields = ['user']
    list_filter = ['user']
    readonly_fields = ['license']

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    def bangLai(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.license.name)
            )


# gia ve
class PriceTAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'date_cate']
    search_fields = ['price', 'date_cate']
    list_filter = ['price', 'date_cate']

    # formfield_overrides = {
    #     PriceT.price: {'widget': admin.widgets.AdminTextInputWidget(attrs={'type': 'number'})},}

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


admin_site = AppAdminSite(name='Quản lý bán vé')

admin_site.register(Car, CarAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Chair, ChairAdmin)

admin_site.register(Province, ProvinceAdmin)
admin_site.register(BStation, BStationAdmin)
admin_site.register(Buses, BusesAdmin)
admin_site.register(Bus_BSta, Bus_BStaAdmin)

admin_site.register(PriceT, PriceTAdmin)
admin_site.register(Trip, TripAdmin)

admin_site.register(Staff, StaffAdmin)
admin_site.register(Customer, CustomerAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Driver, DriverAdmin)


