from telegram.ext import (
    Updater, 
    CommandHandler, MessageHandler, Filters,
)
from config import TOKEN
from handlers import (
    start_command, help_command,
    hendle_settings, hendle_text, hendle_contact, hendle_location, hendle_photo,
)


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
