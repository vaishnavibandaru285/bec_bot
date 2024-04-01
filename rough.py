from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler
import spacy
import subprocess

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

index = "index.py"


# Define the function to handle incoming messages
async def message_handler(update, context):
    # Get the user's message
    user_message = update.message.text

    # Process the user's message using spaCy
    doc = nlp(user_message)

    # Extract the main concepts from the user's message
    main_concepts = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

    # Check if the user's message contains concepts related to admission
    greet = any(
        concept in ["hi", "hello", "good morning", "good afternoon", "good evening", "hlo" ,"hey", "howdy", "greetings", "salutations", "welcome", "hi there", "morning", "afternoon", "evening"] for concept in main_concepts)
    location = any( concept in ["location", "place", "loc", "area", "address", "site", "position", "venue", "vicinity", "district", "region", "neighborhood", "locality", "spot", "address"] for concept in main_concepts)
    is_admission_query = any(
        concept in ["admission", "apply", "join", "application", "seat", "enroll", "admit", "enrollment", "register", "admittance", "admission process", "entry", "admissions office", "registration", "applying"] for concept in main_concepts)
    placement = any(
        concept in ["placements", "job", "placement", "jobs", "placed", "package","career", "employment", "recruitment", "opportunity", "job placement", "career services", "job opportunities", "job market", "employment rate"] for concept in main_concepts)
    courses = any(
        concept in ["course", "courses", "departments", "depart", "cource", "cources", "subj", "subjects", "dept", "computer science", "information technology", "artificial intelligence", "machine learning", "data science", "cybersecurity", "civil engineering", "mechanical engineering", "electrical engineering", "electronics and communication engineering",
                    "depts", "cse", "it", "aiml", "cbds", "cb", "mech", "ece"] for concept in
        main_concepts)
    hostel = any(
        concept in ["hostel","girls", "hostels", "girls hostel", "facilities", "outing", "outings", "hostal", "hostals","accomodation","stay","accommodation", "lodging", "residence", "dormitory", "boarding", "boarding house", "digs", "dorm", "guesthouse", "bed and breakfast", "overnight", "housing", "living quarters", "shelter", "facility", "amenities", "boarding facility", "student living", "college accommodation"] for
        concept in main_concepts)
    transport = any(
        concept in ["bus","college bus", "shuttle service", "campus transport", "bus schedule", "bus route", "bus stop", "bus fare", "bus pass", "bus driver", "bus facility", "transportation service", "shuttle bus", "college transport", "bus timing", "bus pickup", "bus drop-off", "bus route map", "bus registration", "bus availability", "bus capacity"] for
        concept in main_concepts)
    # Construct the response based on the message content
    if is_admission_query:
        button7 = InlineKeyboardButton('Admission Process', callback_data='admission')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif greet:
        response2 = "Hello!How may i help you?"
        await update.message.reply_text(response2)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif placement:
        await update.message.reply_photo(open('p1.jpg', 'rb'),caption="Department wise placed students in the year 2022-23")
        await update.message.reply_photo(open('p2.jpg', 'rb'),caption="Statistics of students placed year wise")

        button7 = InlineKeyboardButton('Placements', callback_data='placements')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("We found this based on your query.", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif location:
        button7 = InlineKeyboardButton('Location', callback_data='location')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("We found this based on your query.", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif transport:
        button7 = InlineKeyboardButton('Facilities', callback_data='facilities')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("We found this based on your query.", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif courses:
        button2 = InlineKeyboardButton('Courses offered', callback_data='courses')
        button9 = InlineKeyboardButton('Departments', callback_data='departments')
        keyboard = InlineKeyboardMarkup([
            [button2, button9]
        ])
        await update.message.reply_text("We found this based on your query.", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif hostel:
        await update.message.reply_photo(open('hostel.jpg', 'rb'),
                                         caption="• BEC uniquely provides on campus hostel facility to its girl student community\n"
                                                 "• This hostel accommodating 1600 girl students is maintained on self-run basis by students themselves.\n"
                                                 "• The residents of hostel are provided with 24 hr hot water supply through solar water heaters.\n"
                                                 "• The students health needs are taken care by dispensary with a visiting doctor and 24/7 ambulance\n")
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
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])






# Define the function to start the bot
async def start(update, context):
    await update.message.reply_text("Welcome to the College Admission Bot! "
                                    "Feel free to ask any questions about admission.")


app = ApplicationBuilder().token("6765202047:AAG_XQ6b0pnt6wHigRDsgzUU9F9Rv3bpYKQ").build()

# Register the command handler and message handler
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(None, callback=message_handler))

# Start the bot by polling
app.run_polling()
