from django.shortcuts import render
from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from django.core.mail  import send_mail
from django.conf import settings

from .models import Rooms, Booking, Category ,CommentRoom ,RestaurantMenu
from .forms import BookingRoomForm , ContactForm , RoomCommentForm, AnswerCommentForm
from ..blog.models import Post
from django.core.paginator import Paginator
from ..account.models import Employees
from datetime import datetime
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
        "posts":posts,
    }

     
    return render (request, "index.html", context)


@login_required
def room_details(request, room_pk):
    room=get_object_or_404(Rooms,pk=room_pk)
    comments=room.comments.filter(parent=None)
    form = BookingRoomForm()
    date=datetime.now()
    rating = room.rating_room  # Remove the parentheses here
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

            text=f"""
            Congratulations! Your Successful Hotel Room Reservation

                Hooray! We are delighted to inform you that your hotel room reservation for [Check-In Date] - [Check-Out Date] has been confirmed. Our warmest congratulations!

                Details of your reservation:

                Guest Name: {booking.user.username}
                Check-In Date: {booking.check_in}
                Check-Out Date: {booking.check_out}
                Room Type: {room.category}
                Nightly Rate: {room.price}
                Total price for the booking: {room_price}
                Number of Adults: {booking.adult}
                Additional Amenities: {room.services}
                About your room:

                {room.info}
                Booking Information:

                Your reservation is confirmed, and we guarantee your room for the specified dates. Please present your booking number at check-in for a quick registration. We recommend keeping this email and booking information in a secure place.

                If you have any questions or need further assistance, don't hesitate to contact our customer support at [Contact Information for Customer Support].

                We look forward to your arrival and hope that your stay at our hotel will be unforgettable and enjoyable. Thank you for choosing our hotel!

                Best Regards,
                Sona Hotel
            """
            send_mail(subject="room booking", message=text, from_email=settings.EMAIL_HOST_USER,recipient_list=[request.user.email])
            


            messages.info(request, "Комната успешно забронированна! Ждём вашего приезда!")
            return render(request, "room-details.html", {"room":room, "form": form, "room_price":room_price})
                
    return render(request, "room-details.html", {"room":room, "form": form,'comments':comments,"date":date, 'rating': rating})


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
def room_comment(request, room_pk):
    room = get_object_or_404(Rooms, pk=room_pk)
    if request.method == "POST":
        form = RoomCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.room = room
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



# def search_rooms(request):
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')

#     if min_price and max_price:
#         rooms = Rooms.filter_by_price_range(min_price, max_price)
#     else:
#         rooms = Rooms.objects.all()

#     return render(request, 'base.html', {'rooms': rooms})


def employees(request):
    employees=Employees.objects.all()


    return render(request, "employees.html", {"eployees":employees})

