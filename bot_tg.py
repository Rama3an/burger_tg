from telegram.utils.request import *
from telegram import *
from telegram.ext import *
from settings import TOKEN
from commands import do_start, do_text, set_time
from keyboard import keyboard_callback_handler


class Bot:
    # Правильное подключение
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        request=request,
        token=TOKEN,
    )
    # Обработчик
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    message_handler_start = CommandHandler('start', do_start)
    updater.dispatcher.add_handler(message_handler_start)

    message_handler_time = CommandHandler('time', set_time)
    updater.dispatcher.add_handler(message_handler_time)

    message_handler_keyboard = CallbackQueryHandler(callback=keyboard_callback_handler,
                                                    pass_chat_data=True)
    updater.dispatcher.add_handler(message_handler_keyboard)

    message_handler = MessageHandler(Filters.text, do_text)
    updater.dispatcher.add_handler(message_handler)

    # Запустить бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()