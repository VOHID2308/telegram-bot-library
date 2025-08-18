import requests
from telegram.ext import (
    Updater, CallbackContext,
    CommandHandler, MessageHandler, Filters,
)
from telegram import Update
from config import TOKEN


def calculate_currency(currency: str, amount: float) -> float:
    response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/')

    data = response.json()
    kurs = float(data[0]['Rate'])

    if currency == 'USD-UZS':
        return kurs * amount
    else:
        return amount / kurs


def start_command(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(f"Salom {user.full_name}! Kurs hisoblovchi botga hush kelibsiz.")


def handle_text(update: Update, context: CallbackContext):
    text = update.message.text
    
    currency, amount = text.split(":")

    result = calculate_currency(currency, float(amount))

    update.message.reply_text(f"Natija: {result:,.2f}")


def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(CommandHandler("start", start_command))

    # message handlers
    dispatcher.add_handler(MessageHandler(Filters.text, handle_text))

    updater.start_polling()
    updater.idle()

main()
