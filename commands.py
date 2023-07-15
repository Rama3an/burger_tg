from telegram import *
from telegram.ext import *
from keyboard import get_person_keyboard, get_ready_keyboard

TIME = 0


def do_start(update: Update, context: CallbackContext):
    message_text = "Привет! Выбери свою роль"

    update.message.reply_text(
        text=message_text,
        reply_markup=get_person_keyboard(),
    )


def set_time(update: Update, context: CallbackContext):
    global TIME
    TIME = update.message.text[6:]


def do_text(update: Update, context: CallbackContext):
    message_text = "Я не понимаю("
    update.message.reply_text(
        text=message_text
    )


def get_result(update: Update, context: CallbackContext):
    message_text = "Выберите ответ"
    update.message.reply_text(
        text=message_text,
        reply_markup=get_ready_keyboard(),
    )
