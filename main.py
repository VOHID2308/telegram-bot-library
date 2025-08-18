from telegram.ext import (
    Updater, CallbackContext, 
    CommandHandler, MessageHandler, Filters,
)
from telegram import Update
from config import TOKEN


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Salom")


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Nima yordam")


def hendle_text(update: Update, context: CallbackContext):
    update.message.reply_text("xabar qabul qilindi")


def hendle_settings(update: Update, context: CallbackContext):
    update.message.reply_text("siz sozlamalar bolimidasiz")


def hendle_contact(update: Update, context: CallbackContext):
    update.message.reply_text("Contact qabul qlindi")


def hendle_location(update: Update, context: CallbackContext):
    update.message.reply_text("Location qabul qilindi")


def hendle_photo(update: Update, context: CallbackContext):
    update.message.reply_text("Rasm qabul tilindi")


def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # message handlers
    dispatcher.add_handler(MessageHandler(Filters.text("sozlamalar"), hendle_settings))
    dispatcher.add_handler(MessageHandler(Filters.text, hendle_text))
    dispatcher.add_handler(MessageHandler(Filters.contact, hendle_contact))
    dispatcher.add_handler(MessageHandler(Filters.location, hendle_location))
    dispatcher.add_handler(MessageHandler(Filters.photo, hendle_photo))

    updater.start_polling()
    updater.idle()

main()
