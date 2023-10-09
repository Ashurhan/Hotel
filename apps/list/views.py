from django.shortcuts import render
from .models import Rooms ,Category


def index(request):
     
    return render (request, "index.html")



def all_rooms(request):
    rooms=Rooms.objects.all()
    
    context={

        "rooms":rooms,
    }

    return render (request, "rooms.html" , context)


