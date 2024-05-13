import uuid

from admin_interface.models import Theme
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.html import format_html
from django import forms
from django.utils.safestring import mark_safe
from .models import Ticket
from .firebase import storage







# class MyServiceStaff(admin.ModelAdmin):
#
#     add_form_template = 'admin/add_form.html'


#my admin
class AppStaff(admin.AdminSite):
    index_title = 'HỆ THỐNG BÁN VÉ XE TRỰC TUYẾN'






staff_site = AppStaff(name='Bán vé')

staff_site.register(Ticket)
# staff_site.register(Theme)



