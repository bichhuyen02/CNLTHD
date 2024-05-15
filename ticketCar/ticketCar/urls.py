"""
URL configuration for ticketCar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home.html
    2. Add a URL to urlpatterns:  path('', Home.html.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from myService import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# import debug_toolbar
from myService.admin import admin_site
from myService.staff import staff_site

schema_view = get_schema_view(
    openapi.Info(
        title="TicketCar API",
        default_version='v1',
        description="APIs for TicketCar",
        contact=openapi.Contact(email="ticketCar@gmail.com"),
        license=openapi.License(name="TicketCar@2024"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('cars', views.CarViewSet, basename='cars')

router.register('priceT', views.PriceTViewSet, basename='priceT')
router.register('invoice', views.InvoiceViewSet, basename='invoice')
router.register('ticket', views.TicketViewSet, basename='ticket')

router.register('province', views.ProvinceViewSet, basename='province')
router.register('trips', views.TripViewSet, basename='trips')
router.register('bStation', views.BStationViewSet, basename='bStation')
router.register('bues', views.BuesViewSet, basename='bues')
router.register('tripCar', views.TripCarViewSet, basename='tripCar')

router.register('complain', views.ComplainViewSet, basename='complain')

router.register('staff', views.StaffViewSet, basename='staff')
router.register('customer', views.CustomerViewSet, basename='customer')
router.register('driver', views.DriverViewSet, basename='driver')
router.register('user', views.UserViewSet, basename='user')





urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),



    path('admin/', admin_site.urls),
    path('staffs/', staff_site.urls),



    re_path(r'^ckeditor/',
            include('ckeditor_uploader.urls')),




    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),

    path('o/', include('oauth2_provider.urls',
    namespace='oauth2_provider')),
]
