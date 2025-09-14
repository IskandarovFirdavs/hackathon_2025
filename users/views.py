from django.shortcuts import render, redirect
from .models import Doctor, Patient, Booking
from .forms import PatientForm, BookingForm

def home(request):
    return render(request, "home.html")

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, "doctors.html", {"doctors": doctors})

def patients(request):
    patients = Patient.objects.all()
    return render(request, "patients.html", {"patients": patients})

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patients")
    else:
        form = PatientForm()
    return render(request, "add_patient.html", {"form": form})

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookings")
    else:
        form = BookingForm()
    return render(request, "booking.html", {"form": form})

def bookings(request):
    bookings = Booking.objects.all()
    return render(request, "bookings.html", {"bookings": bookings})
