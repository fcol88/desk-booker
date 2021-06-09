from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="root"),
    path('home', views.home, name="home"),
    path('bookings/list', views.bookinglist, name="home"),
    path('bookings/form', views.bookingform, name="home"),
    path('locations/list', views.locationlist, name="home"),
    path('locations/form', views.locationform, name="home"),
    path('desks/list', views.desklist, name="home"),
    path('desks/form', views.deskform, name="home"),
]