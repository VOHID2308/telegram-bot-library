from telegram.ext import CallbackContext
from telegram import Update


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