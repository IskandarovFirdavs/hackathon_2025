from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('doctors/', views.doctors, name="doctors"),
    path('patients/', views.patients, name="patients"),
    path('add-patient/', views.add_patient, name="add_patient"),
    path('booking/', views.booking, name="booking"),
    path('bookings/', views.bookings, name="bookings"),
]
