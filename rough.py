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
        concept in ["course", "courses", "departments", "depart", "cource", "cources", "subj", "subjects", "dept",
                    "depts", "cse", "it", "aiml", "cbds", "cb", "mech", "ece"] for concept in
        main_concepts)
    hostel = any(
        concept in ["hostel","girls", "hostels", "girls hostel", "facilities", "outing", "outings", "hostal", "hostals","accomodation","stay"] for
        concept
        in
        main_concepts)

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

    elif life:
        reslife = "The BTech program offers a vibrant campus life with diverse academic, social, and extracurricular activities. Rigorous coursework, experienced faculty, and hands-on learning foster critical thinking and problem-solving skills.\nOutside the classroom, students enjoy a lively social scene with clubs, events, and sports teams, fostering lifelong friendships. Modern facilities, including libraries and labs, support academic success, while career services and internships prepare students for post-graduation success.\n\nOverall, campus life in the BTech program is dynamic, supportive, and provides ample opportunities for personal growth."

        await update.message.reply_text(reslife)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif activites:
        act="Our college offers a vibrant array of clubs and organizations catering to diverse interests and fostering personal development. The Cultural and Creative Arts Club (CCA) celebrates cultural diversity through events such as dance competitions and art exhibitions.\n\nAWAAZ provides a platform for honing public speaking and debate skills through workshops and competitions.\n\nMeanwhile, the National Cadet Corps (NCC) instills discipline, leadership, and patriotism through training and community service.\n\n The National Service Scheme (NSS) engages students in social service activities like cleanliness drives and blood donation camps, promoting social responsibility.\n\n Lastly, the Codeverse Club focuses on computer programming and technology skills development, offering coding workshops and projects to encourage innovation and entrepreneurship. These clubs collectively enrich campus life, providing students with opportunities for growth, engagement, and connection."

        await update.message.reply_text(act)
        button_a = InlineKeyboardButton('Student Activities', callback_data='student')
        keyboard = InlineKeyboardMarkup([
            [button_a]
        ])
        await update.message.reply_text("Also we've found this, based on your query.", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif canteen:
        cant="Our college offers a convenient and diverse canteen facility, providing students with a range of food options to suit their tastes and preferences. The canteen serves a variety of freshly prepared meals, breakfast, ensuring students have access to nutritious and affordable food throughout the day.\n\nWith a spacious and comfortable seating area, students can enjoy their meals in a relaxed environment conducive to socializing and studying. The canteen staff are friendly and attentive, ensuring prompt service and maintaining cleanliness and hygiene standards.\n\n Overall, the canteen facility at our college enhances the campus experience, offering students a convenient dining option to fuel their academic pursuits."

        await update.message.reply_text(cant)
        button_c = InlineKeyboardButton('Canteen', callback_data='canteen')
        keyboard = InlineKeyboardMarkup([
            [button_c]
        ])
        await update.message.reply_text("Also we've found this, based on your query.", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif library:
        lib="Our college offers a comprehensive library system, including a traditional library and a digital library, both offering flexible hours extending until 6 pm in the evening. With this extended access, students can conveniently utilize resources and study materials to enhance their academic pursuits.\n\n The traditional library provides access to a vast collection of physical books, journals, and reference materials, while the digital library offers online resources, e-books, and digital archives accessible from anywhere with an internet connection.\n\n This combination of resources and flexible hours ensures that students have ample opportunities for research, study, and learning outside of regular classroom hours."

        await update.message.reply_text(lib)
        button_l = InlineKeyboardButton('Library', callback_data='library')
        keyboard = InlineKeyboardMarkup([
            [button_l]
        ])
        await update.message.reply_text("Also we've found this, based on your query.", reply_markup=keyboard)
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


#app = ApplicationBuilder().token("6765202047:AAG_XQ6b0pnt6wHigRDsgzUU9F9Rv3bpYKQ").build()
app = ApplicationBuilder().token("6974619344:AAFlRROokqdH3OpIaOtQ32QKGT6PTqrZhZ8").build()

# Register the command handler and message handler
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(None, callback=message_handler))

# Start the bot by polling
app.run_polling()
