import os
from telebot import TeleBot
from telebot.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
from KeyboardButton import * 
from email.mime import image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import string
from importlib.resources import path
from language import *

# ------------imports-----------
commands = [
    BotCommand("start", "start bot"),
    BotCommand("blur", "set blur to photo"),
    BotCommand("language", "set language")
]

# ------------commands-----------

bot = TeleBot("6906386058:AAFWbbFEOvn9BlulLcQYlbJMtzR0Dqgg-Yw")
bot.set_my_commands(commands)