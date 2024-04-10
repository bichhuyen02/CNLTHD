from django.contrib import admin
from django.urls import path
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe

from .models import Car, Customer, Category, Complain, Chair, Staff, BStation, PriceT, Trip, Driver,User
# Register your models here.



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

# class CourseForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget)
#
#     class Meta:
#         model = Course
#         fields = '__all__'
#
# class LessonForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget)
#
#     class Meta:
#         model = Lesson
#         fields = '__all__'


#xe
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class CarAdmin(admin.ModelAdmin):
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

class ChairAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']



#ve
class PriceTAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_cate']
    search_fields = ['date_cate']
    list_filter = ['id', 'date_cate']
    # form = LessonForm
    # inlines = [LessonTagInlineAdmin]

class VeAdmin(admin.ModelAdmin):
    pass




#chuyen xe
class BStationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class TripAdmin(admin.ModelAdmin):
    list_display = ['id', 'timeGo', 'dateGo']
    search_fields = ['timeGo', 'dateGo']
    list_filter = ['timeGo', 'dateGo']




#account
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'firstname', 'lastname']
    search_fields = ['username', 'lastname']
    list_filter = ['username', 'lastname']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'birt', 'user']
    search_fields = ['phone']
    list_filter = ['phone']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'birt', 'user']
    search_fields = ['phone']
    list_filter = ['phone']

class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'birt', 'user']
    search_fields = ['phone']
    list_filter = ['phone']
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

admin_site = AppAdminSite(name='Quản lý bán vé')

admin_site.register(Car, CarAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Chair, ChairAdmin)
# admin_site.register(GiaVe)
admin_site.register(BStation)
admin_site.register(Trip)
admin_site.register(Staff)
admin_site.register(Customer)
admin_site.register(Complain)
admin_site.register(User)
admin_site.register(Driver)
admin_site.register(PriceT)