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
    button9 = InlineKeyboardButton('Departments', callback_data='departments')

    keyboard = InlineKeyboardMarkup([
        [button1, button2],
        [button3, button4],
        [button5, button6],
        [button7, button8],
        [button9]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def about_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('admin.jpg', 'rb'))
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
    button4 = InlineKeyboardButton("Msc", callback_data="msc")
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
        AIML   =>  180
        CB      =>  120
        CIVIL   =>  120
        DS   =>  120
        ECE  => 120
        EEE  => 120
        EIE  => 120
        IT   => 120
        ME   => 120
        """
    await query.message.reply_text(courses_info, parse_mode='Markdown')
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def mtech_button_callback(update , context) ->None:
    query = update.callback_query
    await query.answer()
    courses_info = """
           Course         Seats Available
        Civil =>  6
        CSE   =>  6
        ECE   =>  6
        EEE   =>  6
        ME    =>  6
        """
    await query.message.reply_text(courses_info, parse_mode='Markdown')
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def mca_button_callback(update , context) ->None:
    query = update.callback_query
    await query.answer()
    courses_info = """
           Course         Seats Available
        Civil =>  6
        CSE   =>  6
        ECE   =>  6
        EEE   =>  6
        ME    =>  6
        """
    await query.message.reply_text(courses_info, parse_mode='Markdown')
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
    
async def msc_button_callback(update , context) ->None:
    query = update.callback_query
    await query.answer()
    courses_info = """
           Course         Seats Available
        Civil =>  6
        CSE   =>  6
        ECE   =>  6
        EEE   =>  6
        ME    =>  6
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
    await query.message.reply_text("Bus facilities from routes :\n"
                                   "1.BEC - Bapatla(local) - BEC\n"
                                    "2.BEC - Chirala - Pandillapalli - BEC\n"
                                    "3.BEC - Pharmacy Hostel - BEC")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
    
async def library_button_callback(update , context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('library.jpg', 'rb'),caption = "1.Area - 22,000sq.ft\n"
                                   "2.No. of volumes - 78,972\n"
                                   "3.No. of e-journals - 725\n"
                                   "4.No. of titles - 29,296\n"
                                   "5.No. of print journals - 86\n"
                                   "6.No. of e-books - 858\n"
                                   "7.No. of computer systems - 35\n"
                                   "8.No. of back volumes of journals - 2,969\n"
                                   "9.No. of NPTEL video courses - 236\n"
                                   "10.No. of educational CD's - 3,261")
    await query.message.reply_text("Library timings : 7AM - 6PM")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
    

async def canteen_button_callback(update , context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('canteen.jpg', 'rb'), caption="A hygienic, well-furnished and well-equipped canteen is available in the campus to provide food at subsidized rates for the staff and students. Purified drinking water is supplied in the college, hostel and canteen.")
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
    



app = ApplicationBuilder().token("6765202047:AAG_XQ6b0pnt6wHigRDsgzUU9F9Rv3bpYKQ").build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CallbackQueryHandler(chat_button_callback, pattern='chat'))
app.add_handler(CallbackQueryHandler(about_button_callback, pattern='about'))
app.add_handler(CallbackQueryHandler(courses_button_callback, pattern='courses'))
app.add_handler(CallbackQueryHandler(btech_button_callback, pattern='btech'))
app.add_handler(CallbackQueryHandler(mtech_button_callback, pattern='mtech'))
app.add_handler(CallbackQueryHandler(mca_button_callback, pattern='mca'))
app.add_handler(CallbackQueryHandler(msc_button_callback, pattern='msc'))
app.add_handler(CallbackQueryHandler(facilities_button_callback, pattern='facilities'))
app.add_handler(CallbackQueryHandler(transport_button_callback, pattern='transport'))
app.add_handler(CallbackQueryHandler(library_button_callback, pattern='library'))
app.add_handler(CallbackQueryHandler(canteen_button_callback, pattern='canteen'))
app.add_handler(CallbackQueryHandler(result_button_callback, pattern='result'))
app.add_handler(CallbackQueryHandler(exit_button_callback, pattern='exit'))
app.run_polling()
