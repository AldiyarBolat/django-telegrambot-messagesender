from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from telegram.utils.request import Request
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackContext

from ...models import Profile


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Error :{e}'
            print(error_message)
            raise e
    return inner


@log_errors
def handle_message(update: Update, contex: CallbackContext):
    try:
        profile = Profile.objects.get(token=update.message.text)
        profile.telegram_id = update.message.chat.id
        profile.save()
        reply_text = 'You have successfully connected'
    except ObjectDoesNotExist:
        reply_text = 'No such token exist'

    update.message.reply_text(text=reply_text)


@log_errors
def send_message(chat_id, user_name, text):
    request = Request(
        connect_timeout=1.0,
        read_timeout=1.0,
    )
    bot = Bot(
        request=request,
        token=settings.TOKEN,
        base_url=settings.PROXY_URL,
    )
    bot.sendMessage(chat_id, f'{user_name}, я получил ваше вообщение\n{text}')


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        # Connection
        request = Request(
            connect_timeout=1.0,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )

        print(bot.get_me())

        # Handle
        updater = Updater(
            bot=bot,
            use_context=True,
        )
        message_handler = MessageHandler(Filters.text, handle_message)
        updater.dispatcher.add_handler(message_handler)

        # Run infinitely
        updater.start_polling()
        updater.idle()




