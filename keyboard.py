from telebot import types
from language.keyboard_lang import *


def generate_main_menu(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_powerbank = types.KeyboardButton(text=menu_powerbank[lang])
    btn_back = types.KeyboardButton(back[lang])
    keyboard.row(btn_powerbank)
    keyboard.row(btn_back)
    return keyboard


def generate_language():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_uz = types.KeyboardButton(text="UZ🇺🇿")
    btn_ru = types.KeyboardButton(text="RU🇷🇺")
    keyboard.row(btn_uz, btn_ru)
    return keyboard


def generate_inline_url(url, lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_more = types.InlineKeyboardButton(text=more[lang], url=url)
    btn_more_bay = types.InlineKeyboardButton(text=buy[lang], callback_data="buy")
    keyboard.row(btn_more_bay, btn_more)
    return keyboard


def generate_url(url, lang='uz'):
    keyboard = types.InlineKeyboardMarkup()
    btn_more = types.InlineKeyboardButton(text=more[lang], url=url)
    keyboard.row(btn_more)
    return keyboard


def generate_pagination(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_next = types.KeyboardButton(text=nextt[lang])
    btn_prev = types.KeyboardButton(text=bacck[lang])
    btn_menu = types.KeyboardButton(text=back_to[lang])
    keyboard.row(btn_prev, btn_next)
    keyboard.row(btn_menu)
    return keyboard
