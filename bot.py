from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
BOT_TOKEN = 'Y7699996331:AAHK8AWzaOqgd1K2XoyFDYukAYI7RUCTyo8'
updater = Updater(BOT_TOKEN)

# Define the start command function
def start(update: Update, context: CallbackContext) -> None:
    # Define the button that opens your Web App link
    keyboard = [
        [InlineKeyboardButton("View Airdrops", web_app=WebAppInfo(url="https://airdropworld.netlify.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Click below to view the latest airdrops!", reply_markup=reply_markup)

# Add the start command handler
updater.dispatcher.add_handler(CommandHandler("start", start))

# Start the bot
updater.start_polling()
updater.idle()
