from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from ...models import Rooms

def main_markups():
    markup=InlineKeyboardMarkup(row_width=2)
    buttons=[
        InlineKeyboardButton("All rooms" ,callback_data="all_rooms")

    ]
    markup.add(*buttons)
    return markup

def rooms_markup(rooms: list[Rooms]):
    markup = InlineKeyboardMarkup(row_width=2)
    for room in rooms:
        
        button = InlineKeyboardButton(text=room.category.name, callback_data=f"{room.id}")    
        markup.add(button)
    return markup


