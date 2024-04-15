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
    import re

    # Define a regular expression pattern for greetings

    greet= re.compile(
        r'\b(hi|hello|good\s+morning|good\s+afternoon|good\s+evening|hlo|hey|howdy|greetings|salutations|welcome|hi\s+there)\b',
        re.IGNORECASE)
    location= re.compile(
        r'\b(?:location|place|loc|area|address|site|position|venue|vicinity|district|region|neighborhood|locality|spot)\b',
        re.IGNORECASE)
    is_admission_query= re.compile(
        r'\b(?:admission|apply|join|application|seat|enroll|admit|enrollment|register|admittance|'
        r'admission\s+process|entry|admissions\s+office|registration|applying)\b',
        re.IGNORECASE)

    placement_it = re.compile(
        r'\b(?:placements\s+in\s+it|it\s+placements|jobs\s+in\s+it|placed\s+in\s+it|package\s+in\s+it)\b',
        re.IGNORECASE)


    placement_it_24 = re.compile(
        r'\b(?:it\s+2023-2024|it\s+2023-24|2023-2024\s+it|2023-24\s+it)\b',
        re.IGNORECASE)

    placement_cse = re.compile(
        r'\b(?:placements\s+in\s+cse|cse\s+placements|jobs\s+in\s+cse|placed\s+in\s+cse|package\s+in\s+cse|cse\s+in\s+2022-2023|cse\s+2022-23)\b',
        re.IGNORECASE)

    placement_ece = re.compile(
        r'\b(?:placements\s+in\s+ece|ece\s+placements|jobs\s+in\s+ece|placed\s+in\s+ece|package\s+in\s+ece)\b',
        re.IGNORECASE)

    placement_eee = re.compile(
        r'\b(?:placements\s+in\s+eee|eee\s+placements|jobs\s+in\s+eee|placed\s+in\s+eee|package\s+in\s+eee)\b',
        re.IGNORECASE)

    placement= re.compile(
        r'\b(?:placements|job|placement|jobs|placed|package|career|employment|recruitment|'
        r'opportunity|job\s+placement|career\s+services|job\s+opportunities|job\s+market|employment\s+rate)\b',
        re.IGNORECASE)
    courses= re.compile(r'\b(?:course|courses|departments|dept|cource|cources|subj|subjects'
                        r'|dept|computer\s+science|information\s+technology|artificial\s+intelligence|'
                        r'machine\s+learning|data\s+science|cyber\s+security|civil\s+engineering|mechanical\s+engineering|'
                        r'electrical\s+engineering|electronics\s+and\s+communication\s+engineering|depts|cse|it|aiml|cbds|cb|mech|ece)\b', re.IGNORECASE)
    library = re.compile(
        r'\b(?:library|libraries|digital|lib|Lib|Books|Reading|Knowledge|Information|Resources|Archives|'
        r'Catalog|Collection|Reference|Librarian|Research|Literacy|Database|Periodicals|Multimedia|Archives|Study|'
        r'Digitalization|E-books|Audiobooks|Manuscripts|Interlibrary\s+loan|Education|Librarianship|Library\s+card)\b',
        re.IGNORECASE)

    canteen12 = re.compile(
        r'\b(?:canteen|special|menu|food|meals|breakfast|lunch|snack|Cafeteria|Dining|Catering|Refreshments'
        r'|Beverages|Cuisine|Culinary|Buffet|Takeout|Dining\s+hall|Foodservice|Vending|Cooking|Nutritious|Ingredients|'
        r'Menu\s+options|Dietary\s+restrictions|Meal\s+plans|Food\s+quality|Chef|Food\s+safety|Serving|Ordering'
        r'|Budget\s+friendly|Variety|Hospitality\s+industry)\b',
        re.IGNORECASE)

    activities= re.compile(
        r'\b(?:clubs|organization|recreation|leisure|non\s+academic|extra\s+curricular|Sports|'
        r'Events|Workshops|Competitions|Games|Performances|Exercise|Hobbies|Art|Crafts|Dance|Music|Volunteering|'
        r'Socializing|Clubs|Societies|Associations|Teams|Adventure|Travel|Adventure\s+sports|Team\s+building'
        r'|Skill\s+development|Networking|Entertainment|Outdoor\s+activities|Indoor\s+activities)\b',
        re.IGNORECASE)

    life = re.compile(r'\b(?:culture|atmosphere|ambiance|environment|life)\b', re.IGNORECASE)

    transport= re.compile(
        r'\b(?:bus|college\s+bus|shuttle\s+service|campus\s+transport|bus\s+schedule|bus\s+route'
        r'|bus\s+stop|bus\s+fare|bus\s+pass|bus\s+driver|bus\s+facility|transportation\s+service|shuttle\s+bus|'
        r'college\s+transport|bus\s+timing|bus\s+pickup|bus\s+drop\s+off|bus\s+route\s+map|bus\s+registration'
        r'|bus\s+availability|bus\s+capacity|transport|transport\s+facility|transport\s+facilities)\b',
        re.IGNORECASE)

    hostel= re.compile(
        r'\b(?:girls|girls\s+hostel|girls\s+accomodation'
        r'|girls\s+stay|girls\s+lodging|girls\s+residence|girls\s+dormitory'
        r'college\s+accommodation)\b',
        re.IGNORECASE)

    boys_hostel = re.compile(
        r'\b(?:boys|gents|gent|boy\s+hostel|boys\s+hostals|boys\s+accomodation'
        r'|male|boys\s+residence|male\s+residence|boys\s+hostel)\b',
        re.IGNORECASE)

    # Construct the response based on the message content
    if is_admission_query.search(user_message):
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

    elif greet.search(user_message):
        response2 = "Hello!How may i help you?"
        await update.message.reply_text(response2)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no_button')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif placement_it.search(user_message):
        await update.message.reply_photo(open('IT.png', 'rb'),
                                         caption="Percentage of students placed in the year 2022 , 2023 & 2024")
        await update.message.reply_text("31 students from Information Technology have placed in the year 2022-2023.\n"
                                        "Below are the companies , which have recruited the students from information Technology :\n"
                                        "* Tata Consultancy Services(Ninja)\n"
                                        "* Tata Consultancy Service (Digital)\n"
                                        "* Delloit\n"
                                        "* Hexaware Technologies\n"
                                        "* Snovasys\n"
                                        "* Talent Pace Pvt. Ltd.\n"
                                        "* KJ Systems\n"
                                        "* Virtusa\n"
                                        "* CareMonitor\n"
                                        "* Mitsogo\n"
                                        "* Eflair Technologies\n"
                                        "* BrighTex Bio-Photonics(BTBP)\n"
                                        "* TuringMinds")

        button7 = InlineKeyboardButton('Placements', callback_data='placements')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("To Know more about placements in BEC, click the below button", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif placement_it_24.search(user_message):
        await update.message.reply_photo(open('IT.png', 'rb'),
                                         caption="Percentage of students placed in the year 2022 , 2023 & 2024")
        await update.message.reply_text("22 students from Information Technology have placed in the year 2023-2024.\n"
                                        "Below are the companies , which have recruited the students from information Technology :\n"
                                        "* Accenture\n"
                                        "* T-Machine software solutions\n"
                                        "* ExcelR solutions\n"
                                        "* Snovasys\n"
                                        "* Numetry Technologies\n"
                                        "* KJ systems")

        button7 = InlineKeyboardButton('Placements', callback_data='placements')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("To Know more about placements in BEC, click the below button", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif placement_cse.search(user_message):
        await update.message.reply_photo(open('cse.png', 'rb'),
                                         caption="Percentage of students placed in the year 2022 , 2023 & 2024")
        await update.message.reply_text("96 students from Computer Science & Engineering have placed in the year 2022-2023.\n"
                                        "Below are the companies , which have recruited the students from Computer Science & Engineering :\n"
                                        "* Tata Consultancy Services(Ninja)\n"
                                        "* Tata Consultancy Service (Digital)\n"
                                        "* Delloit\n"
                                        "* Hexaware Technologies\n"
                                        "* Snovasys\n"
                                        "* Talent Pace Pvt. Ltd.\n"
                                        "* KJ Systems\n"
                                        "* CareMonitor\n"
                                        "* Eflair Technologies\n"
                                        "* TuringMinds\n"
                                        "* ThunderSoft\n"
                                        "* Polomon Instruments pvt. ltd.\n"
                                        "* Efftronics\n"
                                        "* Tech Mahindra\n"
                                        "* Cadsys")

        button7 = InlineKeyboardButton('Placements', callback_data='placements')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("To Know more about placements in BEC, click the below button", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif placement_ece.search(user_message):
        await update.message.reply_photo(open('ECE.png', 'rb'),
                                         caption="Percentage of students placed in the year 2022 , 2023 & 2024")
        await update.message.reply_text("21 students from Electronics & Communication Engineering have placed in the year 2022-2023.\n"
                                        "Below are the companies , which have recruited the students from Electronics & Communication Engineering :\n"
                                        "* Tata Consultancy Services(Ninja)\n"
                                        "* Tata Consultancy Service (Digital)\n"
                                        "* Deloitte consulting services\n"
                                        "* System soft\n"
                                        "* Birla soft\n"
                                        "* HCL Tech"
                                        "* Hexaware Technologies\n"
                                        "* Code young\n"
                                        "* Tech Mahindra\n"
                                        "* ThunderSoft\n")

        button7 = InlineKeyboardButton('Placements', callback_data='placements')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("To Know more about placements in BEC, click the below button", reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif placement_eee.search(user_message):
        await update.message.reply_photo(open('eee_placement.png', 'rb'),
                                         caption="EEE : Percentage of students placed in the year 2022 , 2023 & 2024")
        button7 = InlineKeyboardButton('Placements', callback_data='placements')
        keyboard = InlineKeyboardMarkup([
            [button7]
        ])
        await update.message.reply_text("To Know more about placements in BEC, click the below button",
                                        reply_markup=keyboard)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])


    elif placement.search(user_message):
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

    elif location.search(user_message):
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

    elif transport.search(user_message):
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

    elif courses.search(user_message):
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

    elif hostel.search(user_message):
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

    elif boys_hostel.search(user_message):
        await update.message.reply_text("No, BEC does not provide accomodation facilities for male students.\n"
                                        "Click the below button to know more about facilities provided in Bapatla Enginnering College")
        button_facility = InlineKeyboardButton('Facilities', callback_data='facilities')

        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button_facility],
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif life.search(user_message):
        reslife = "The BTech program offers a vibrant campus life with diverse academic, social, and extracurricular activities. Rigorous coursework, experienced faculty, and hands-on learning foster critical thinking and problem-solving skills.\nOutside the classroom, students enjoy a lively social scene with clubs, events, and sports teams, fostering lifelong friendships. Modern facilities, including libraries and labs, support academic success, while career services and internships prepare students for post-graduation success.\n\nOverall, campus life in the BTech program is dynamic, supportive, and provides ample opportunities for personal growth."

        await update.message.reply_text(reslife)
        button1 = InlineKeyboardButton('Yes', callback_data='queries')
        button2 = InlineKeyboardButton('No', callback_data='no')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)
        subprocess.run(['python', index])

    elif activities.search(user_message):
        act = "Our college offers a vibrant array of clubs and organizations catering to diverse interests and fostering personal development. The Cultural and Creative Arts Club (CCA) celebrates cultural diversity through events such as dance competitions and art exhibitions.\n\nAWAAZ provides a platform for honing public speaking and debate skills through workshops and competitions.\n\nMeanwhile, the National Cadet Corps (NCC) instills discipline, leadership, and patriotism through training and community service.\n\n The National Service Scheme (NSS) engages students in social service activities like cleanliness drives and blood donation camps, promoting social responsibility.\n\n Lastly, the Codeverse Club focuses on computer programming and technology skills development, offering coding workshops and projects to encourage innovation and entrepreneurship. These clubs collectively enrich campus life, providing students with opportunities for growth, engagement, and connection."

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
        await update.message.reply_text("Do you need further assistance?",
                                        reply_markup=keyboard)
        subprocess.run(['python', index])

    elif canteen12.search(user_message):
        response = "Our college offers a convenient and diverse canteen facility, providing students with a range of food options to suit their tastes and preferences. The canteen serves a variety of freshly prepared meals, breakfast, ensuring students have access to nutritious and affordable food throughout the day.\n\nWith a spacious and comfortable seating area, students can enjoy their meals in a relaxed environment conducive to socializing and studying. The canteen staff are friendly and attentive, ensuring prompt service and maintaining cleanliness and hygiene standards.\n\n Overall, the canteen facility at our college enhances the campus experience, offering students a convenient dining option to fuel their academic pursuits."

        await update.message.reply_text(response)
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
        subprocess.run(['python',index])

    elif library.search(user_message):
        lib = "Our college offers a comprehensive library system, including a traditional library and a digital library, both offering flexible hours extending until 6 pm in the evening. With this extended access, students can conveniently utilize resources and study materials to enhance their academic pursuits.\n\n The traditional library provides access to a vast collection of physical books, journals, and reference materials, while the digital library offers online resources, e-books, and digital archives accessible from anywhere with an internet connection.\n\n This combination of resources and flexible hours ensures that students have ample opportunities for research, study, and learning outside of regular classroom hours."

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
        button2 = InlineKeyboardButton('No', callback_data='no_button')
        keyboard = InlineKeyboardMarkup([
            [button1, button2]
        ])
        await update.message.reply_text("Do you need further assistance?", reply_markup=keyboard)



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
