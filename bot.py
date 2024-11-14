from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

# Create an Application object
application = Application.builder().token("7699996331:AAHK8AWzaOqgd1K2XoyFDYukAYI7RUCTyo8").build()

# Define the start command function
async def start(update: Update, context: CallbackContext) -> None:
    # Define the button that opens your Web App link
    keyboard = [
        [InlineKeyboardButton("View Airdrops", web_app=WebAppInfo(url="https://airdropworld.netlify.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click below to view the latest airdrops!", reply_markup=reply_markup)

# Add command handler
application.add_handler(CommandHandler("start", start))

# Run the bot
application.run_polling()