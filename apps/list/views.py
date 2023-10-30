from django.shortcuts import render
from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.core.mail  import send_mail
from django.conf import settings

from .models import Rooms, Booking, Category ,CommentRoom
from .forms import BookingRoomForm , ContactForm , RoomCommentForm, AnswerCommentForm
from ..blog.models import Post
from django.core.paginator import Paginator

import datetime
from .filters import RoomsFilter

# from forms import ContactForm
login_required
def index(request):
    rooms=Rooms.objects.all()
    categories=Category.objects.all()
    posts=Post.objects.all()

    myFilter=RoomsFilter(request.GET, queryset=rooms)

    context={
        "rooms":rooms,
        "categories": categories,
        "myFilter": myFilter,
        "posts":posts
    }

     
    return render (request, "index.html", context)


@login_required
def room_details(request, room_pk):
    room=get_object_or_404(Rooms,pk=room_pk)
    comments=room.comments.filter(parent=None)
    form = BookingRoomForm()
    room_price=0
    if request.method == "POST":    
        form = BookingRoomForm(request.POST)
        if form.is_valid():
                    
            if room.status == "not_available":
                messages.error(request, "Данная комната на данный момент недоступна для бронирования.")
                # return redirect("room_details", room_pk=room.pk)
                return render(request, "room-details.html", {"room":room, "form": form,'comments':comments})
            
            check_in = form.cleaned_data.get("check_in")
            check_out = form.cleaned_data.get("check_out")

            existing_bookings = Booking.objects.filter(room=room)

            for booking in existing_bookings:
                if booking.check_out >= check_in and booking.check_in <= check_out:
                    messages.error(request, "Данная комната уже забронирована в эту дату. Выберите другую.")
                    return render(request, "room-details.html", {"room": room, "form": form,'comments':comments})
            day = (check_out - check_in).days
            room_price= room.price*day
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            room.save()


            send_mail(subject="room booking", message="succes", from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
            


            messages.info(request, "Комната успешно забронированна! Ждём вашего приезда!")
            return render(request, "room-details.html", {"room":room, "form": form, "room_price":room_price})
                
    return render(request, "room-details.html", {"room":room, "form": form,'comments':comments})


@login_required
def all_rooms(request):
    rooms=Rooms.objects.all()


    myFilter=RoomsFilter(request.GET, queryset=rooms)
    rooms=myFilter.qs

    paginator = Paginator(rooms, 6)

    page = request.GET.get("page")
    rooms = paginator.get_page(page)
    context={

        "rooms":rooms,
    }

    return render (request, "rooms.html" , context)

@login_required
def about_us(request):
    room=Rooms.objects.all()
    context={
        "room":room
    }
     
    return render (request, "about-us.html", context)

    

login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact') 
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})





    


    



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


@login_required
def room_comment(request,room_pk):
    room=get_object_or_404(Rooms, pk=room_pk)
    if request.method=="POST":
        form=RoomCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.room = room  # Set the post for the comment
            comment.save()
            return redirect("room_details", room_pk=room.pk)
        return render(request, 'room-details.html', {'form': form, 'room': room})

@login_required    
def answer_comment(request, comment_id):
    parent_comment = get_object_or_404(CommentRoom, pk=comment_id)
    
    if request.method == "POST":
        form =AnswerCommentForm (request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent = parent_comment
            comment.post_id = parent_comment.post_id
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    
    form = AnswerCommentForm()
    return render(request, "room-details.html", {"form": form, "parent_comment": parent_comment})


@login_required
def delete_comment(request, comment_pk):
    comment= CommentRoom.objects.get(pk=comment_pk)
    
    if comment not in request.user.room_commnets.all():
        return redirect("room_details", room_pk=comment.room.pk)
    
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER'))


