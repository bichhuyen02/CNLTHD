import uuid

from admin_interface.models import Theme
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Ticket
from .firebase import storage







class MyServiceStaff(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        if request.user.role == 'Staff':
            print(2)
            return True
        return False



#my admin
class AppStaff(admin.AdminSite):
    index_title = 'HỆ THỐNG BÁN VÉ XE TRỰC TUYẾN'

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





staff_site = AppStaff(name='Bán vé')

staff_site.register(Ticket)
staff_site.register(Theme)



