from django.db import models
from ..account.models import User



class Contact(models.Model):
    name=models.CharField(max_length=50, null=False)
    email=models.CharField(max_length=100, null=False )
    message=models.CharField(max_length=1000, null=True)
    phone=models.CharField("номер телефона",max_length=14, null=False)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField("назвние", max_length=50)
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="категории"

    def __str__(self):
        return  f"{self.name}"
        
class Rooms(models.Model):
    
    
    info=models.CharField("Описание", max_length=120 , null=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    size=models.SmallIntegerField("размер" , null=True)
    services=models.CharField("сервисы",max_length=100, null=True)
    bed=models.CharField("кровать", max_length=120, null=True)
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="rooms")
    persons=models.CharField("persons",max_length=20, null=True)
     
    class Meta:
        verbose_name="Номер"
        verbose_name_plural= "Номера"
    
    def __str__(self):
        return self.id
    
    

class RoomIMage(models.Model):
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="images")
    room_image=models.ImageField(upload_to="media")


class Booking(models.Model):
    customer = models.ForeignKey(Contact, on_delete=models.CASCADE,null=True, related_name="bookings")
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, related_name="bookings")
    check_in = models.DateField("Дата заезда", null=True)
    check_out = models.DateField("Дата выезда", null=True)
    adult = models.PositiveSmallIntegerField("Adult",null=True,default=1)
    children = models.PositiveSmallIntegerField("Children",null=True, default=0 )
    sum = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    room = models.ForeignKey(Rooms, related_name="rooms", null=True, blank=True,on_delete=models.SET_NULL)
    # status = models.CharField("Status", choices=BOOKING_STATUSES, max_length=10, default=BOOKING_STATUS_DRAFT)
    created = models.DateTimeField("Created",auto_now_add=True, null=True )
