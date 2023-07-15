from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
import commands
import time

CALLBACK_BUTTON_ADMIN = "callback_button_admin"
CALLBACK_BUTTON_EMPLOYEE = "callback_button_employee"
CALLBACK_BUTTON_GOOD = "callback_button_good"
CALLBACK_BUTTON_FAIL = "callback_button_fail"

TITLES = {
    CALLBACK_BUTTON_ADMIN: "Управляющий",
    CALLBACK_BUTTON_EMPLOYEE: "Подчиненный",
    CALLBACK_BUTTON_GOOD: "Выполнено",
    CALLBACK_BUTTON_FAIL: "Не выполнено"
}


def get_person_keyboard():
    keyword = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_ADMIN],
                                 callback_data=CALLBACK_BUTTON_ADMIN)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_EMPLOYEE],
                                 callback_data=CALLBACK_BUTTON_EMPLOYEE)
        ]
    ]
    return InlineKeyboardMarkup(keyword)


def get_ready_keyboard():
    keyword = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_GOOD],
                                 callback_data=CALLBACK_BUTTON_GOOD)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_FAIL],
                                 callback_data=CALLBACK_BUTTON_FAIL)
        ]
    ]
    return InlineKeyboardMarkup(keyword)


def keyboard_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    TIME = commands.TIME
    ADMIN = 0

    if data == CALLBACK_BUTTON_ADMIN:
        ADMIN = 1
        query.edit_message_text(text="Спасибо!")
        update.effective_message.reply_text(text="Введите время дедлайна")
    elif data == CALLBACK_BUTTON_EMPLOYEE:
        query.edit_message_text(text="Спасибо!")
        update.effective_message.reply_text(
            text="Выберите результат",
            reply_markup=get_ready_keyboard()
        )
    elif data == CALLBACK_BUTTON_GOOD:
        try:
            if (time.localtime().tm_hour * 60 + time.localtime().tm_min) - (
                    int(TIME[:2]) * 60 + int(TIME[3:])) <= 0:
                query.edit_message_text(text="Молодец!")
                if ADMIN == 1:
                    update.effective_message.reply_text("Задание выполнено")
            else:
                query.edit_message_text(text="Не успели")
                if ADMIN == 0:
                    update.effective_message.reply_text("Задание не выполнено")
        except:
            update.effective_message.reply_text(text="Дедлайн не был задан")
    elif data == CALLBACK_BUTTON_FAIL:
        query.edit_message_text(text="Жаль(")
        if ADMIN == 0:
            update.effective_message.reply_text("Задание не выполнено")
