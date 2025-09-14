from django.contrib import admin
from .models import Doctor, Patient, Booking

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty")
    search_fields = ("name", "specialty")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "contact")
    search_fields = ("name", "contact")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "time")
    list_filter = ("doctor", "date")
    search_fields = ("patient__name", "doctor__name")
