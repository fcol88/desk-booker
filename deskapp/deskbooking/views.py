from django.shortcuts import render
from deskbooking import validators

def home(request):

    return render(request, 'deskbooking/home.html',
                    { 'selected' : 'home' })

def bookinglist(request):

    return render(request, 'deskbooking/bookings/list.html',
                    { 'selected' : 'bookings' })

def bookingform(request):

    if request.method == "POST":
        validators.validate_booking(request)

    return render(request, 'deskbooking/bookings/form.html',
                    { 'selected' : 'bookingform' })

def locationlist(request):

    return render(request, 'deskbooking/locations/list.html',
                    { 'selected' : 'locations' })

def locationform(request):

    return render(request, 'deskbooking/locations/form.html',
                    { 'selected' : 'locationform' })

def desklist(request):

    return render(request, 'deskbooking/desks/list.html',
                    { 'selected' : 'desks' })

def deskform(request):

    return render(request, 'deskbooking/desks/form.html',
                    { 'selected' : 'deskform' })