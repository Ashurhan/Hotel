from django.db import models
from ..account.models import User


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    message = models.CharField(max_length=1000, null=True)
    phone = models.CharField("номер телефона", max_length=14, null=False)



    
    def __str__(self):
        return self.name
    

    
class Category(models.Model):
    name=models.CharField("назвние", max_length=50)
    class Meta:
        verbose_name="Категория "
        verbose_name_plural="категории"

    def __str__(self):
        return  f"{self.name}"




class Rooms(models.Model):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    NOT_AVAILABLE = "not_available"

    ROOM_STATUSES = [
        (AVAILABLE, "available"),
        (OCCUPIED, "occupied"),
        (NOT_AVAILABLE, "not available")
    ]
    
    info=models.TextField("описание", null=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    size=models.SmallIntegerField("размер" , null=True)
    services=models.TextField("сервисы", null=True)
    bed=models.CharField("кровать", max_length=120, null=True)
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="rooms")
    persons=models.CharField("persons",max_length=20, null=True)
    status=models.CharField("Статус", max_length=15, choices=ROOM_STATUSES, default=AVAILABLE)
     
    class Meta:
        verbose_name="Номер"
        verbose_name_plural= "Номера"
    
    def __str__(self):
        return f" {self.id}-{self.category}"

    
    @property
    def rating_room(self):
        comments = self.comments.all()
        
        if comments:
            rating_sum = sum(comment.rating for comment in comments)
            total_rating = rating_sum / len(comments)
            return total_rating
        else:
            return 0.0

    @staticmethod
    def filter_by_price_range(min_price, max_price):
        return Rooms.objects.filter(price__gte=min_price, price__lte=max_price)

    def __str__(self):
        return f"Room {self.id} - {self.category}"
    

class RoomIMage(models.Model):
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="images")
    room_image=models.ImageField(upload_to="media")

    def __str__(self):
        return f"{self.id}- {self.room}"


class Booking(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, related_name="bookings")
    room = models.ForeignKey(Rooms, related_name="rooms", null=True, blank=True,on_delete=models.SET_NULL)
    check_in = models.DateField("Дата заезда", null=True)
    check_out = models.DateField("Дата выезда", null=True)
    adult = models.PositiveSmallIntegerField("Adult",null=True,default=1)
    children = models.PositiveSmallIntegerField("Children",null=True, default=0 )
    created = models.DateTimeField("Created",auto_now_add=True, null=True )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self) -> str:
        return f"{self.user} - {self.check_in}:{self.check_out}"


class CommentRoom(models.Model):
    author=models.ForeignKey(User, related_name="room_commnets", on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name="comments")
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey("self", on_delete=models.CASCADE, related_name="sybcommnets", null=True, blank=True)
    rating=models.SmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name="Коментария комнаты"
        verbose_name_plural="Коментария комнаты"

   
    



class RestaurantBook(models.Model):
    name=models.CharField(max_length=100,null=False,default=None)
    phone = models.CharField("Номер телефона", max_length=14,null=False)
    email = models.CharField(max_length=100,null=False)
    time = models.DateTimeField("Время брони", null=True)
    persons = models.PositiveSmallIntegerField("Persons",null=True,default=1)
    message=models.TextField(max_length=2000,null=True)


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def str(self):
        return f"{self.name}"


class RestaurantMenu(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name="m_category",null=True)
    price  = models.DecimalField(max_digits=20, decimal_places=2)
    info = models.TextField("Описание")


class RestaurantImage(models.Model):
    restaurant=models.ForeignKey(RestaurantMenu,related_name="restaurant", null=True, blank=True,on_delete=models.SET_NULL)
    restaurantimage=models.ImageField(upload_to="media/")

    