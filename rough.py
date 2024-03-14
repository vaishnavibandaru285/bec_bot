from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler , CallbackQueryHandler
import spacy
import subprocess

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

index = "C:/Users/vaish/Desktop/bec_bot/index.py"
# Define the function to handle incoming messages
async def message_handler(update, context):
    # Get the user's message
    user_message = update.message.text
    
    # Process the user's message using spaCy
    doc = nlp(user_message)
    
    # Extract the main concepts from the user's message
    main_concepts = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

    # Check if the user's message contains concepts related to admission

    is_admission_query = any(concept in ["admission", "apply", "join", "application", "seat", "enroll"] for concept in main_concepts)
    placement = any(concept in ["placements", "job", "offers", "placement", "offer", "jobs"] for concept in main_concepts)

    # Construct the response based on the message content
    if is_admission_query:
        response1 = "To get admission in our college, you can apply through EAMCET, " \
                   "lateral entry by ECET, or through a donation."
        await update.message.reply_text(response1)
        #await update.message.reply_text("Would you like to continue our conversation?")
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])


    else:
        # Default response if the message does not contain relevant information
        response2 = "Sorry, I'm still learning. I can only provide information about admissions."
        # Send the response back to the user
        await update.message.reply_text(response2)

'''async def yes_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton('Click to enter query', callback_data='queries')

    keyboard = InlineKeyboardMarkup([
        [button1]
    ])
    await query.message.reply_text("Click the button to chat", reply_markup=keyboard)
    subprocess.run(['python', index])'''


async def no_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
    subprocess.run(['python', index])

# Define the function to start the bot
async def start(update, context):
    await update.message.reply_text("Welcome to the College Admission Bot! "
                                    "Feel free to ask any questions about admission.")


app = ApplicationBuilder().token("6765202047:AAG_XQ6b0pnt6wHigRDsgzUU9F9Rv3bpYKQ").build()

# Register the command handler and message handler
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(None,callback=message_handler))
#app.add_handler(CallbackQueryHandler(yes_button_callback, pattern='yes'))
app.add_handler(CallbackQueryHandler(no_button_callback, pattern='no'))

# Start the bot by polling
app.run_polling()