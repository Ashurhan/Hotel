from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Rooms
from telebot import TeleBot
from telebot import types
from .markups import main_markups, rooms_markup


# Объявление переменной бота
bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)

@bot.message_handler(commands=["start"])
def start(message):
    text=(
        "hello World"
    )
    markup=main_markups()
    bot.send_message(chat_id=message.chat.id ,text=text, reply_markup=markup ) 



@bot.callback_query_handler(lambda call : call.data=="all_rooms")
def show_rooms(call:types.CallbackQuery ):
    rooms=Rooms.objects.all() 
    
    markup=rooms_markup(rooms)
           
    bot.send_message(chat_id=call.message.chat.id , text="вот все комнаты", reply_markup=markup)






@bot.callback_query_handler(lambda call: call.data.isdigit())
def room_details(call : types.CallbackQuery):
    room=Rooms.objects.get(id=int(call.data))
    text=f"""
        room category-{room.category}
        room image-{room.images}
        room price-{room.price} $
        room size-{room.size} ft
        room services-{room.services}
        room size-{room.bed}
        room persons -{room.persons}
        you want to booking {"http://127.0.0.1:8000/room_details/1"}
        """
    bot.send_message(chat_id=call.message.chat.id, text=text)
    
                                                                                                                                                                                                                                                                                                                                                                                                                                        

# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()				# Загрузка обработчиков
        bot.infinity_polling()	
