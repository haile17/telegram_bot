from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from flask import Flask, request
import os

app = Flask(__name__)

# Create an Application object
application = Application.builder().token("7699996331:AAHK8AWzaOqgd1K2XoyFDYukAYI7RUCTyo8").build()

# Define the start command function
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Airdrops", callback_data="airdrop")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an option below:", reply_markup=reply_markup)

# Define the button press handler
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the click

    if query.data == "airdrop":
        await query.edit_message_text(text="You clicked on Airdrops!")

# Add command and callback handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))

# Set up webhook route for Flask
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, application.bot)
    application.process_update(update)
    return '', 200

# Set webhook (Update with your actual deployed URL)
application.bot.set_webhook(url="https://airdropworld.netlify.app/")

# Start the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)