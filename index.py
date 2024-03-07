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
    button10 = InlineKeyboardButton('Location', callback_data='location')
    button11 = InlineKeyboardButton('Contact Us', callback_data='contact')


    keyboard = InlineKeyboardMarkup([
        [button1, button2],
        [button3, button4],
        [button5, button6],
        [button7, button8],
        [button10,button11],
        [button9]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def about_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('bec_bot/admin.jpg', 'rb'))
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
    
async def placements_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('ci.jpg','rb'))
    await query.message.reply_photo(open('ci1.jpg','rb'))
    await query.message.reply_photo(open('ci2.jpg','rb'))
    await query.message.reply_photo(open('ci3.jpg','rb'))
    await query.message.reply_photo(open('ci4.jpg','rb'))                                                                                                                              
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

async def rankings_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("You've clicked Rankings")
    if query.data == 'rankings':
        with open("bec_bot/NAAC.jpg", 'rb') as photo:
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=photo)
    await query.message.reply_text("""
      🌟Our college is thrilled to announce our recent achievement of an NAAC A+ grade 🏆 with a remarkable score of 3.49 out of 4 in 2023! Additionally, we have consistently secured an NBA ranking over the past 10 years, reinforcing our commitment to excellence in technical and professional education 🛠️📈. 
                                   
       This stellar NAAC rating, alongside our sustained NBA recognition, celebrates our steadfast commitment to academic excellence 📚, cutting-edge teaching methodologies 🎓, and holistic student support 🤝. 
                                   
       We're proud to solidify our status as a leading institution in higher education, shining bright as a beacon of quality and innovation in learning. 🌈💫
                                   """)
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def admission_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("You've clicked Admission process")
    await query.message.reply_text(""" 
    🌈 EAMCET Gateway 🚀: Unlock your future with admissions through the prestigious Engineering, Agriculture, and Medical Common Entrance Test. Dive into your dream career with us!

    🏗️ Advance with ECET 🎓: Elevate your technical expertise! Diploma holders can leap into engineering degrees through the Engineering Common Entrance Test.

    🤍 Empowering Specially-Abled Students ♿: Our inclusive seats ensure a barrier-free, empowering learning journey for specially-abled achievers. Your potential is limitless here!

    ✨ Flexible Donation Seats 🏫: Missed EAMCET or ECET? No worries! Our donation seats offer a second chance to step into your desired field. Plus, donation contributions are branch-specific, ensuring opportunities are as diverse as your dreams.
                                   
    🎉 A Nurturing Academic Environment 📚: We're more than a college; we're a community committed to fostering diversity, excellence, and innovation. Join us to create, inspire, and succeed together!
    """)
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def student_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("You've clicked Student Activities")
    await query.message.reply_text("""🏛️Join the vibrant student community at our college, where you'll discover an array of opportunities to engage and grow through our diverse range of clubs and activities. Whether you're drawn to community service, leadership development, cultural expression, or creative arts, there's a welcoming space for you to explore and thrive in.

    👮🏽‍♂️Immerse yourself in the spirit of service with clubs like the National Cadet Corps (NCC) and National Service Scheme (NSS), where you can make a meaningful impact through various community initiatives and projects. Develop valuable leadership skills and forge lifelong friendships as you work together towards common goals.

    🎭Indulge your passion for the arts and unleash your creativity with the Creative Arts Club (CCA) and Literary Club(Awaaz). Whether you're an aspiring artist, writer, musician, or actor, you'll find endless opportunities, collaborate with fellow enthusiasts, and showcase your talents to the world.
                                   
    🏛️Codeverse, the coding club at your college, offers a dynamic platform for students to enhance their coding skills, engage in practical projects, and connect with like-minded peers.Through participation in coding challenges, and mentorship opportunities, members gain invaluable experience and preparation for tech careers.

    🏛️At our college, the learning doesn't stop at the classroom door. Join us and be a part of an enriching college experience that goes beyond academics, where you can discover your passions, develop new skills, and create memories that will last a lifetime. Come, be a part of our vibrant community and embark on a journey of self-discovery and personal growth.""")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def location_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("You've clicked Location")
    await query.message.reply_text("You can navigate through this Google location:\n\n\n https://maps.app.goo.gl/8Xoox4DaG4gd5ZBX7")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def contact_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("You've clicked Contact Us")
    await query.message.reply_text(""" 
    Bapatla Engineering College
    Bapatla-522101,
    Guntur(Dt).,
    Phone : +91-8643-224244
    Mobile No: +91-9440730035
    Fax : +91-8643-224246
    email:: bec_principal@yahoo.com
            bec_principal@becbapatla.ac.in                 
                        
    Official pages: https://www.becbapatla.ac.in                                 

    Connect us via:
    Instagram:: https://www.instagram.com/becbapatlaofficial?igsh=MTNzdWFxZjFjYmxqMA==
                                   
    Facebook:: https://www.facebook.com/becbapatlaofficial/
                                   
    Twitter:: #BapatlaC
                                      
    """)
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


app = ApplicationBuilder().token("6765202047:AAG_XQ6b0pnt6wHigRDsgzUU9F9Rv3bpYKQ").build()
#app = ApplicationBuilder().token("6974619344:AAFlRROokqdH3OpIaOtQ32QKGT6PTqrZhZ8").build()


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
app.add_handler(CallbackQueryHandler(placements_button_callback, pattern='placements'))
app.add_handler(CallbackQueryHandler(departments_button_callback, pattern='departments'))
app.add_handler(CallbackQueryHandler(rankings_button_callback, pattern='rankings'))
app.add_handler(CallbackQueryHandler(student_button_callback, pattern='student'))
app.add_handler(CallbackQueryHandler(admission_button_callback, pattern='admission'))
app.add_handler(CallbackQueryHandler(location_button_callback, pattern='location'))
app.add_handler(CallbackQueryHandler(contact_button_callback, pattern='contact'))

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