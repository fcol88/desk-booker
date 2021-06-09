from django.contrib import messages
from datetime import date

def validate_booking(request):

    booking_date_day = request.POST.get('booking_date_day', '')
    booking_date_month = request.POST.get('booking_date_month', '')
    booking_date_year = request.POST.get('booking_date_year', '')
    booking_location = request.POST.get('booking_location', '')
    booking_desk = request.POST.get('booking_desk', '')
    date_is_valid = True

    if booking_date_day == '':
        messages.add_message(request, messages.WARNING, "Enter a day")
        date_is_valid = False
    
    if booking_date_month == '':
        messages.add_message(request, messages.WARNING, "Enter a month")
        date_is_valid = False

    if booking_date_year == '':
        messages.add_message(request, messages.WARNING, "Enter a year")
        date_is_valid = False

    if booking_location == '':
        messages.add_message(request, messages.WARNING, "Choose a location")

    if booking_desk == '':
        messages.add_message(request, messages.WARNING, "Choose an available desk")

    if date_is_valid == True:
        try:
            booking_date = date(year=booking_date_year,month=booking_date_month,day=booking_date_day)
            if booking_date < date.today():
                messages.add_message(request, messages.WARNING, "Enter a today's date or a future date")
                return None
            return booking_date
        except ValueError:
            messages.add_message(request, messages.WARNING, "Enter a valid date")    
    return None

def validate_location(request):

    location_name = request.POST.get('location_name', '')

    if location_name == '':
        messages.add_message(request, messages.WARNING, "Enter a location name")

    return location_name.strip()

def validate_desk(request):

    desk_identifier = request.POST.get('desk_identifier', '')
    
    if desk_identifier == '':
        messages.add_message(request, messages.WARNING, "Enter a desk number")

    return desk_identifier.strip()
    