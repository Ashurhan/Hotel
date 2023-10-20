from django.shortcuts import render
from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Rooms, Booking 
from .forms import BookingRoomForm , ContactForm ,CommentForm

import datetime

# from forms import ContactForm

def index(request):
    rooms=Rooms.objects.all()
    context={
        "rooms":rooms
    }
     
    return render (request, "index.html", context)


@login_required
def room_details(request, room_pk):
    room=get_object_or_404(Rooms,pk=room_pk)
    form = BookingRoomForm()
    if request.method == "POST":    
        form = BookingRoomForm(request.POST)
        if form.is_valid():        
            if room.status == "not_available":
                messages.error(request, "Данная комната на данный момент недоступна для бронирования.")
                return render(request, "room-details.html", {"room":room, "form": form})
            
            check_in = form.cleaned_data.get("check_in")
            check_out = form.cleaned_data.get("check_out")

            existing_bookings = Booking.objects.filter(room=room)

            for booking in existing_bookings:
                if booking.check_out >= check_in and booking.check_in <= check_out:
                    messages.error(request, "Данная комната уже забронирована в эту дату. Выберите другую.")
                    return render(request, "room-details.html", {"room": room, "form": form})


            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            room.save()
            messages.info(request, "Уомната успешно забронированна! Ждём вашего приезда!")
            return render(request, "room-details.html", {"room":room, "form": form})
                
    return render(request, "room-details.html", {"room":room, "form": form})



def all_rooms(request):
    rooms=Rooms.objects.all()
    
    context={

        "rooms":rooms,
    }

    return render (request, "rooms.html" , context)


def about_us(request):
    room=Rooms.objects.all()
    context={
        "room":room
    }
     
    return render (request, "about-us.html", context)

    



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # contact=form.save(commit=False)
            contact = form.save()
            return redirect('contact')  
    else:
        form = ContactForm()  

    return render(request, "contact.html", {"form": form})








@login_required
def write_comments(request):
    if request.method =="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user
            comment.save()
            return redirect("blog-details")
    



@login_required
def booking_index(request):
    room=get_object_or_404(Rooms)
    form = BookingRoomForm()
    if request.method == "POST":    
        form = BookingRoomForm(request.POST)
        if form.is_valid():        
            if room.status == "not_available":
                messages.error(request, "Данная комната на данный момент недоступна для бронирования.")
                return render(request, "index.html", {"room":room, "form": form})
            
            check_in = form.cleaned_data.get("check_in")
            check_out = form.cleaned_data.get("check_out")

            existing_bookings = Booking.objects.filter(room=room)

            for booking in existing_bookings:
                if booking.check_out >= check_in and booking.check_in <= check_out:
                    messages.error(request, "Данная комната уже забронирована в эту дату. Выберите другую.")
                    return render(request, "index.html", {"room": room, "form": form})


            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            room.save()
            messages.info(request, "Уомната успешно забронированна! Ждём вашего приезда!")
            return render(request, "index.html", {"room":room, "form": form})
                
    return render(request, "index.html", {"room":room, "form": form})


