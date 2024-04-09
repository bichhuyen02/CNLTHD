from django.contrib import admin
from django.urls import path
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe

from .models import Xe, LoaiXe, Ghe, GiaVe, BenXe, ChuyenXe, User, NhanVien, KhachHang, Complain
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
class LoaiXeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class XeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bienSo']
    search_fields = ['name']
    list_filter = ['id', 'bienSo']
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

class GheAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']



#ve
class GiaVeAdmin(admin.ModelAdmin):
    list_display = ['id', 'loai']
    search_fields = ['loai']
    list_filter = ['id', 'loai']
    # form = LessonForm
    # inlines = [LessonTagInlineAdmin]

class VeAdmin(admin.ModelAdmin):
    pass





#chuyen xe
class BenXeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class ChuyenXeAdmin(admin.ModelAdmin):
    list_display = ['id', 'gioXP', 'ngayXP']
    search_fields = ['gioXP', 'ngayXP']
    list_filter = ['gioXP', 'ngayXP']




#account
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'firstname', 'lastname']
    search_fields = ['username', 'lastname']
    list_filter = ['username', 'lastname']

class KhachHangAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'birt', 'user']
    search_fields = ['phone']
    list_filter = ['phone']

class NhanVienAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'birt', 'user']
    search_fields = ['phone']
    list_filter = ['phone']

class TaiXeAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'birt', 'user']
    search_fields = ['phone']
    list_filter = ['phone']
    readonly_fields = ['bangLai']

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    def bangLai(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.bangLai.name)
            )

admin_site = AppAdminSite(name='Quản lý bán vé')

admin_site.register(Xe)
admin_site.register(LoaiXe)
admin_site.register(Ghe)
# admin_site.register(GiaVe)
admin_site.register(BenXe)
admin_site.register(ChuyenXe)
admin_site.register(NhanVien)
admin_site.register(KhachHang)
admin_site.register(Complain)
admin_site.register(User)