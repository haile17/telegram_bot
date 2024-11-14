from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext


# Create an Application object
application = Application.builder().token("7699996331:AAHK8AWzaOqgd1K2XoyFDYukAYI7RUCTyo8").build()

# Define the start command function
async def start(update: Update, context: CallbackContext) -> None:
    # Define the inline buttons
    keyboard = [
        [
            InlineKeyboardButton("Airdrops", callback_data="airdrop"),
            InlineKeyboardButton("Other Option", callback_data="other_option"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send a message with the inline buttons
    await update.message.reply_text("Choose an option below:", reply_markup=reply_markup)

# Define the button press handler
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the click

    # Handle the button action
    if query.data == "airdrop":
        await query.edit_message_text(text="You clicked on Airdrops!")
    elif query.data == "other_option":
        await query.edit_message_text(text="You clicked on Other Option!")

# Add command handler for "/start"
application.add_handler(CommandHandler("start", start))

# Add the handler for the button clicks
application.add_handler(CallbackQueryHandler(button))

# Run the bot
application.run_polling()