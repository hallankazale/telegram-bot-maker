import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Bot-Mestre ativo! Envie /addbot TOKEN para criar um novo bot.")

def addbot(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Envie: /addbot TOKEN_DO_BOT")
        return

    token = context.args[0]
    update.message.reply_text(f"Bot com token {token} registrado! (placeholder)")

def main():
    token = os.getenv("MASTER_BOT_TOKEN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("addbot", addbot))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
