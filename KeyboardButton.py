from telebot.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup


#------------------------------ Choose the language ----------------
def markup_inline():
  markup = InlineKeyboardMarkup()
  markup.width = 2
  markup.add ( InlineKeyboardButton("🇸🇦 العربيه", callback_data="ar"),InlineKeyboardButton("🇺🇸 English", callback_data="en"),)
  markup.add (InlineKeyboardButton("Русский 🇷🇺", callback_data="ru"))

  return markup

#----------------------------Help-----------------------------------

def markup_inline_help():
  markup_help = InlineKeyboardMarkup()
  markup_help.add(InlineKeyboardButton("Lail 🧑‍💻 💙", url="https://t.me/Big_lail"))
  markup_help.add(InlineKeyboardButton("Channel 📢", url="https://t.me/@XTLAIL"))

  return markup_help


  