from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello👋  {update.effective_user.first_name}\n\n")
    button1 = InlineKeyboardButton('Chat', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    keyboard = InlineKeyboardMarkup([
        [button1,button2]
    ])
    await update.message.reply_text("Please select an option:", reply_markup=keyboard)

async def exit_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton('Chat', callback_data='chat')
    keyboard = InlineKeyboardMarkup([
        [button1]
    ])
    await query.message.reply_text("Have a nice day\n"
                                   "Click here to chat again", reply_markup=keyboard)


async def chat_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton('About', callback_data='about')
    button2 = InlineKeyboardButton('Courses offered', callback_data='courses')
    button3 = InlineKeyboardButton('Facilities', callback_data='facilities')
    button4 = InlineKeyboardButton('Rankings', callback_data='rankings')
    button5 = InlineKeyboardButton('Student Activities', callback_data='student')
    button6 = InlineKeyboardButton('Result', callback_data='result')
    button7 = InlineKeyboardButton('Placements', callback_data='placements')
    button8 = InlineKeyboardButton('Admission process', callback_data='admission')
    button9 = InlineKeyboardButton('Fee Structure', callback_data='fee')
    button10 = InlineKeyboardButton('Faculty', callback_data='faculty')
    button11 = InlineKeyboardButton('Departments', callback_data='departments')

    keyboard = InlineKeyboardMarkup([
        [button1, button2],
        [button3, button4],
        [button5, button6],
        [button7, button8],
        [button9, button10],
        [button11]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def about_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("🏛️The Bapatla Engineering College(Autonomous).\n\n"
                                   "🏛️One of the seven educational institutions sponsored by the Bapatla Education Society.\n\n"
                                   "🏛️Established in 1981 with a vision to impart quality technical education.\n\n"
                                   "🏛️Affiliated to Acharya Nagarjuna University.\n\n"
                                   "🏛️The College is a little away from the din and bustle of Bapatla, a town with a historic and hoary past, about 75 Km. south of Vijayawada on Chennai-Vijayawada rail route.\n\n"
                                   "🏛️The college offers B.Tech. Programmes in 8 branches of Engineering:\n"
                                   "1.Artificial Intelligence and Machine Learning\n2.Civil\n3.Computer Science\n4.Cyber Security\n5.Data Science\n6.Electrical and Communication\n7.Electrical and Electronics\n8.Electronics and Instrumentation\n9.Information Technology\n10.Mechanical Engineering.\n")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def courses_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton("B.Tech", callback_data="btech")
    button2 = InlineKeyboardButton("M.Tech", callback_data="mtech")
    button3 = InlineKeyboardButton("MCA", callback_data="mca")
    button4 = InlineKeyboardButton("Diploma", callback_data="diploma")
    keyboard = InlineKeyboardMarkup(
        [
            [button1, button2],
            [button3, button4]
        ]
    )
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def btech_button_callback(update , context) ->None:
    query = update.callback_query
    await query.answer()
    courses_info = """
           Course         Seats Available
        CSE   =>  180
        IT      =>  120
        ECE   =>  120
        EEE   =>  120
        """
    await query.message.reply_text(courses_info, parse_mode='Markdown')
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def facilities_button_callback(update , context) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton("Transport", callback_data="transport")
    button2 = InlineKeyboardButton("Library", callback_data="library")
    button3 = InlineKeyboardButton("Ground", callback_data="ground")
    button4 = InlineKeyboardButton("Canteen", callback_data="canteen")
    button5 = InlineKeyboardButton("Ladies Hostel", callback_data="hostel")
    button6 = InlineKeyboardButton("Dispensary", callback_data="dispensary")
    keyboard = InlineKeyboardMarkup(
        [
            [button1, button2],
            [button3, button4],
            [button5, button6]
        ]
    )
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def transport_button_callback(update , context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("1.BEC - Bapatla(local) - BEC\n"
                                    "2.BEC - Chirala - Pandillapalli - BEC\n"
                                    "3.BEC - Pharmacy Hostel - BEC")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
async def canteen_button_callback(update , context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("A hygienic, well-furnished and well-equipped canteen is available in the campus to provide food at subsidized rates for the staff and students. Purified drinking water is supplied in the college, hostel and canteen.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

    
async def result_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("http://www.becbapatla.ac.in:8080/html/results.html")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
    
async def placements_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()

    await query.message.reply_text("The Training & Placement Cell is committed to provide all possible assistance to the graduate and post-graduate students to secure employment in multi-national companies and other reputed organizations and industries.\n\n"
                                    "This Cell helps the students to improve skills in related fields (soft skills, resume preparation, practice for interviews, etc) and career guidance.\n\n"
                                    "Frequently this cell conducts number of mock tests to improve the performance in written examinations. The aim is to ensure that students have the information and skills necessary for an effective job search.\n\n"
                                    "Training & Placement Officer\n\n"
                                    "BapatlaEngineeringCollege(www.becbapatla.ac.in)\n\n"
                                    "Bapatla, Guntur(Dt), AndhraPradesh - 522101.\n\n"
                                    "Mobile:: 9849409947\n\n"
                                    "Phone:: 08643224244\n\n"
                                    "email:: becplacements@yahoo.com\n\n"
                                            "placements@becbapatla.ac.in\n")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
async def departments_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton("CIVIL", callback_data="civil")
    button2 = InlineKeyboardButton("CB&DS,AI&ML", callback_data="cyber")
    button3 = InlineKeyboardButton("CSE", callback_data="computer")
    button4 = InlineKeyboardButton("ECE", callback_data="electronics")
    button5 = InlineKeyboardButton("EEE", callback_data="electrical")
    button6 = InlineKeyboardButton("EIE", callback_data="instruments")
    button7 = InlineKeyboardButton("IT", callback_data="information")
    button8 = InlineKeyboardButton("MECH", callback_data="mech")

    keyboard = InlineKeyboardMarkup(
        [
            [button1, button2],
            [button3, button4],
            [button5, button6],
            [button7, button8]
        ]
    )
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def information_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("information technology.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
async def computer_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("computer science & engineering.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def electronics_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("electronics & communication engineering.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def civil_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("civil engineering.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def mech_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("mechanical engineering.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
async def cyber_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("cyber security & Data science,Artificial intelligence & machine learning")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def electrical_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("electrical & electronics engineering")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def instruments_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("electronics and instruments.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


app = ApplicationBuilder().token("6765202047:AAG_XQ6b0pnt6wHigRDsgzUU9F9Rv3bpYKQ").build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(chat_button_callback, pattern='chat'))
app.add_handler(CallbackQueryHandler(about_button_callback, pattern='about'))
app.add_handler(CallbackQueryHandler(courses_button_callback, pattern='courses'))
app.add_handler(CallbackQueryHandler(btech_button_callback, pattern='btech'))
app.add_handler(CallbackQueryHandler(facilities_button_callback, pattern='facilities'))
app.add_handler(CallbackQueryHandler(transport_button_callback, pattern='transport'))
app.add_handler(CallbackQueryHandler(canteen_button_callback, pattern='canteen'))
app.add_handler(CallbackQueryHandler(result_button_callback, pattern='result'))
app.add_handler(CallbackQueryHandler(placements_button_callback, pattern='placements'))
app.add_handler(CallbackQueryHandler(departments_button_callback, pattern='departments'))
app.add_handler(CallbackQueryHandler(information_button_callback, pattern='information'))
app.add_handler(CallbackQueryHandler(computer_button_callback, pattern='computer'))
app.add_handler(CallbackQueryHandler(electronics_button_callback, pattern='electronics'))
app.add_handler(CallbackQueryHandler(civil_button_callback, pattern='civil'))
app.add_handler(CallbackQueryHandler(mech_button_callback, pattern='mech'))
app.add_handler(CallbackQueryHandler(cyber_button_callback, pattern='cyber'))
app.add_handler(CallbackQueryHandler(electrical_button_callback, pattern='electrical'))
app.add_handler(CallbackQueryHandler(instruments_button_callback, pattern='instruments'))
app.add_handler(CallbackQueryHandler(exit_button_callback, pattern='exit'))
app.run_polling()
