from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler
import subprocess

rough = "rough.py"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello👋  {update.effective_user.first_name}\n\n")
    button1 = InlineKeyboardButton('Chat', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await update.message.reply_text("Please select an option:", reply_markup=keyboard)

async def exit_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton('Chat', callback_data='chat')
    keyboard = InlineKeyboardMarkup([
        [button1]
    ])
    await query.message.reply_text(f"Have a nice day! {update.effective_user.first_name}\n\n"
                                   "Feel free to visit again\n", reply_markup=keyboard)


async def chat_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton('About', callback_data='about')
    button2 = InlineKeyboardButton('Courses offered', callback_data='courses')
    button3 = InlineKeyboardButton('Facilities', callback_data='facilities')
    button4 = InlineKeyboardButton('Rankings', callback_data='rankings')
    button5 = InlineKeyboardButton('Student Activities', callback_data='student')
    button7 = InlineKeyboardButton('Placements', callback_data='placements')
    button8 = InlineKeyboardButton('Admission process', callback_data='admission')
    button9 = InlineKeyboardButton('Departments', callback_data='departments')
    button10 = InlineKeyboardButton('Location', callback_data='location')
    button11 = InlineKeyboardButton('Contact Us', callback_data='contact')
    button12 = InlineKeyboardButton('Any queries?', callback_data='queries')

    keyboard = InlineKeyboardMarkup([
        [button1, button2],
        [button3, button4],
        [button5],
        [button7, button8],
        [button10, button11],
        [button9],
        [button12]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def about_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('admin.jpg', 'rb') , caption =
    "🏛️The Bapatla Engineering College(Autonomous).\n\n"
    "🏛️One of the seven educational institutions sponsored by the Bapatla Education Society.\n\n"
    "🏛️Established in 1981 with a vision to impart quality technical education.\n\n"
    "🏛️Affiliated to Acharya Nagarjuna University.\n\n"
    "🏆 Certifications: ISO 9001:2015\n\n🏆 NAAC A+ (2023)\n\n🌟 Recognition: Best Engineering College (Careers360)\n\n"
    "🏛️The college is located a bit outside the busy area of Bapatla, a town with a long and storied history. It's around 75 km south of Vijayawada, along the Chennai-Vijayawada railway route.\n\n"
    "🏛️The college offers B.Tech. Programmes in 9 branches of Engineering:\n"
    "1.Computer Science Engineering \n2.Information Technology\n3.Artificial Intelligence and Machine Learning\n4.Cyber Security\n5.Data Science\n6.Electrical and Communication Engineering\n7.Electrical and Electronics Engineering\n8.Civil Engineering \n9.Mechanical Engineering.\n"
    "\n\n🏆 Legacy: 42 years of excellence as one of the engineering colleges under the Bapatla Education Society.\n")

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
    button5 = InlineKeyboardButton("Diploma", callback_data="diploma")
    button3 = InlineKeyboardButton("MCA", callback_data="mca")
    button4 = InlineKeyboardButton("Msc", callback_data="msc")
    keyboard = InlineKeyboardMarkup(
        [
            [button1, button2],
            [button5],
            [button3, button4]
        ]
    )
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def btech_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('Bachelor of Technology.jpg', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def mtech_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('Master of Technology.jpg', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def diploma_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('Diploma.jpg', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def mca_button_callback(update, context) -> None:
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


async def msc_button_callback(update, context) -> None:
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


async def facilities_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    button1 = InlineKeyboardButton("Transport", callback_data="transport")
    button2 = InlineKeyboardButton("Library", callback_data="library")
    button4 = InlineKeyboardButton("Canteen", callback_data="canteen")
    button5 = InlineKeyboardButton("Ladies Hostel", callback_data="hostel")
    button6 = InlineKeyboardButton("Dispensary", callback_data="dispensary")
    keyboard = InlineKeyboardMarkup(
        [
            [button1, button2],
            [button4],
            [button5, button6]
        ]
    )
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def transport_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('bus.jpg', 'rb'), caption= "Bus facilities from routes :\n"
                                   "1.BEC - Bapatla(local) - BEC\n"
                                   "2.BEC - Chirala - Pandillapalli - BEC\n"
                                   "3.BEC - Pharmacy Hostel - BEC\n"
                                    "Total no. of buses available - 11")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def library_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('library.jpg', 'rb'))
    await query.message.reply_photo(open('dlic.jpg', 'rb'))
    await query.message.reply_photo(open('library-volume-table.jpeg', 'rb'))                                                               
    await query.message.reply_text("Library timings : 7AM - 6PM")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def canteen_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('canteen.jpg', 'rb'),
                                    caption="A hygienic, well-furnished and well-equipped canteen is available in the campus to provide food at subsidized rates for the staff and students. Purified drinking water is supplied in the college, hostel and canteen.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def hostel_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('hostel.jpg', 'rb'),
                                    caption="BEC uniquely provides on campus hostel facility to its girl student community\n"
                                            "This hostel accommodating 1600 girl students is maintained on self-run basis by students themselves.\n"
                                            "The residents of hostel are provided with 24 hr hot water supply through solar water heaters.\n"
                                            "The students health needs are taken care by dispensary with a visiting doctor and 24/7 ambulance\n")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def dispensary_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_photo(open('geb.jpg', 'rb'),
                                    caption="BEC recognizes that physical and mental health significantly influences one’s ability to participate fully in the College community.\n"
                                            "The Health Center strives to enhance each student’s well being by providing comprehensive, private health care and by encouraging informed, individual involvement on health related decisions.\n"
                                            "The college has a dispensary to dispose first-aid to students and staff\n"
                                            "A doctor visits college on regular basis to be available to residents of on campus Girls Hostel.\n"
                                            "The College also has a dedicated Ambulance service to meet medical emergencies, if any. The students can utilize preferential treatment service by visiting the hospital of visiting doctor in town anytime.")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
async def placements_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("The following companies have offered opportunities to our college.")   
    await query.message.reply_photo(open('company.jpg','rb'))                                                                                                                              
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
    button2 = InlineKeyboardButton("CB", callback_data="cyber")
    button3 = InlineKeyboardButton("DS", callback_data="ds")
    button4 = InlineKeyboardButton("AI&ML", callback_data="aiml")
    button5 = InlineKeyboardButton("CSE", callback_data="computer")
    button6 = InlineKeyboardButton("ECE", callback_data="electronics")
    button7 = InlineKeyboardButton("EEE", callback_data="electrical")
    button8 = InlineKeyboardButton("EIE", callback_data="instruments")
    button9 = InlineKeyboardButton("IT", callback_data="information")
    button10 = InlineKeyboardButton("MECH", callback_data="mech")

    keyboard = InlineKeyboardMarkup(
        [
            [button1, button2],
            [button3, button4],
            [button5, button6],
            [button7, button8],
            [button9, button10]
        ]
    )
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def civil_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Civil Engineering\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 23\n\n"
                                   "2.No. of non-teaching staff - 5")
    await query.message.reply_document(document=open('civil.pdf', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def cb_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Cyber Security\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 3\n\n")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)
async def ds_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Data Science\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 2\n\n")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def cse_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Computer Science Engineering\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 33\n\n"
                                   "2.1.No. of non-teaching staff - 5")
    await query.message.reply_document(document=open('cse.pdf', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def it_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Information Technology\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 17\n\n"
                                   "2.No. of non-teaching staff - 1")
    await query.message.reply_document(document=open('it.pdf', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def aiml_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Artificial Intelligence & Machine Learning\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 2\n\n")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)


async def mech_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Mechanical Engineering\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 25\n\n"
                                   "2.No. of non-teaching staff - 8")
    await query.message.reply_document(document=open('ME_R20_Syllabus.pdf', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def ece_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Electronics and Communication Engineering\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 31\n\n")
    await query.message.reply_document(document=open('R20-SYLLABUS-FINAL.pdf', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def eee_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Electrical & Electronics Engineering\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 25\n\n"
                                   "2.No. of non-teaching staff - 10")
    await query.message.reply_document(document=open('eee.pdf', 'rb'))
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def eie_button_callback(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Electronics & Instrumentation Engineering\n\n"
                                   "Total no. of Staff :\n\n"
                                   "1.No. of teaching staff - 7\n\n"
                                   "2.No. of non-teaching staff - 3")
    await query.message.reply_document(document=open('eie.pdf', 'rb'))
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
    #await query.message.reply_photo(open("ranking.jpg", 'rb'))
    await query.message.reply_photo(open("NAAC.jpg", 'rb'),caption=
    """
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

    cse = InlineKeyboardButton('CSE', callback_data='admcse')
    it = InlineKeyboardButton('IT', callback_data='admit')
    cs = InlineKeyboardButton('CS', callback_data='admcs')
    csm = InlineKeyboardButton('CS&M', callback_data='admcyberml')
    ds = InlineKeyboardButton('DS', callback_data='admds')
    ece = InlineKeyboardButton('ECE', callback_data='admece')
    eee = InlineKeyboardButton('EEE', callback_data='admeee')
    civil = InlineKeyboardButton('CIVIL', callback_data='admcivil')
    mech = InlineKeyboardButton('MECH', callback_data='admmech')

    keyboard_b = InlineKeyboardMarkup([
        [cse,it],
        [cs,csm],
        [ds],
        [ece,eee],
        [civil,mech]
    ])
    await query.message.reply_text("::::\n\n Choose a branch to get cut-off rank details in EAPCET \n\n::::", reply_markup=keyboard_b)

    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')

    keyboard = InlineKeyboardMarkup([
        [button1, button2]
    ])
    await query.message.reply_text("Please select an option:", reply_markup=keyboard)

async def admcse(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Computer Science Engineering")
    await query.message.reply_photo(open('CSE eapcet.jpg', 'rb'), caption= "cutoff rank for CSE dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)

async def admit(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Information Technology")
    await query.message.reply_photo(open('IT eapcet.jpg', 'rb'), caption= "cutoff rank for IT dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)

async def admcs(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Cyber Security")
    await query.message.reply_photo(open('CS eapcet.jpg', 'rb'), caption= "cutoff rank for CS dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)

async def admcsml(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Cyber Security & Machine learning")
    await query.message.reply_photo(open('CSM eapcet.jpg', 'rb'), caption= "cutoff rank for CSM dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)

async def admds(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Data Science")
    await query.message.reply_photo(open('DS eapcet.jpg', 'rb'), caption= "cutoff rank for DS dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)


async def admece(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Electronics and Communication Engineering")
    await query.message.reply_photo(open('ECE eapcet.jpg', 'rb'), caption= "cutoff rank for ECE dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)

async def admeee(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Electrics & Electronics Engineering")
    await query.message.reply_photo(open('EEE eapcet.jpg', 'rb'), caption= "cutoff rank for EEE dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)

async def admcivil(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen CIVIL Engineering")
    await query.message.reply_photo(open('CIVIL eapcet.jpg', 'rb'), caption= "cutoff rank for CIVIL dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)

async def admmech(update, context) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("you have choosen Mechanical Engineering")
    await query.message.reply_photo(open('MECH eapcet.jpg', 'rb'), caption= "cutoff rank for MECH dept. in the year 2022-23")
    button1 = InlineKeyboardButton('Menu', callback_data='chat')
    button2 = InlineKeyboardButton('Exit', callback_data='exit')
    button3 = InlineKeyboardButton('Back to Admission Process', callback_data='admission')
    keyboard = InlineKeyboardMarkup([
        [button3],
        [button1, button2]
    ])
    await query.message.reply_text("Please choose an option to continue:", reply_markup=keyboard)


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
    await query.message.reply_text(
        "You can navigate through this Google location:\n\n\n https://maps.app.goo.gl/8Xoox4DaG4gd5ZBX7")
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


async def queries_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(" Please enter your query or question, and I'll do my best to assist you.")
    subprocess.run(['python', rough])


#app = ApplicationBuilder().token("6765202047:AAG_XQ6b0pnt6wHigRDsgzUU9F9Rv3bpYKQ").build()
app = ApplicationBuilder().token("6974619344:AAFlRROokqdH3OpIaOtQ32QKGT6PTqrZhZ8").build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(chat_button_callback, pattern='chat'))
app.add_handler(CallbackQueryHandler(about_button_callback, pattern='about'))
app.add_handler(CallbackQueryHandler(courses_button_callback, pattern='courses'))
app.add_handler(CallbackQueryHandler(btech_button_callback, pattern='btech'))
app.add_handler(CallbackQueryHandler(mtech_button_callback, pattern='mtech'))
app.add_handler(CallbackQueryHandler(diploma_button_callback, pattern='diploma'))
app.add_handler(CallbackQueryHandler(mca_button_callback, pattern='mca'))
app.add_handler(CallbackQueryHandler(msc_button_callback, pattern='msc'))
app.add_handler(CallbackQueryHandler(facilities_button_callback, pattern='facilities'))
app.add_handler(CallbackQueryHandler(transport_button_callback, pattern='transport'))
app.add_handler(CallbackQueryHandler(library_button_callback, pattern='library'))
app.add_handler(CallbackQueryHandler(canteen_button_callback, pattern='canteen'))
app.add_handler(CallbackQueryHandler(hostel_button_callback, pattern='hostel'))
app.add_handler(CallbackQueryHandler(dispensary_button_callback, pattern='dispensary'))
app.add_handler(CallbackQueryHandler(placements_button_callback, pattern='placements'))
app.add_handler(CallbackQueryHandler(departments_button_callback, pattern='departments'))
app.add_handler(CallbackQueryHandler(rankings_button_callback, pattern='rankings'))
app.add_handler(CallbackQueryHandler(student_button_callback, pattern='student'))
app.add_handler(CallbackQueryHandler(admission_button_callback, pattern='admission'))
app.add_handler(CallbackQueryHandler(location_button_callback, pattern='location'))
app.add_handler(CallbackQueryHandler(contact_button_callback, pattern='contact'))
app.add_handler(CallbackQueryHandler(queries_button_callback, pattern='queries'))
app.add_handler(CallbackQueryHandler(it_button_callback, pattern='it'))
app.add_handler(CallbackQueryHandler(cse_button_callback, pattern='cse'))
app.add_handler(CallbackQueryHandler(civil_button_callback, pattern='civil'))
app.add_handler(CallbackQueryHandler(mech_button_callback, pattern='mech'))
app.add_handler(CallbackQueryHandler(cb_button_callback, pattern='cb'))
app.add_handler(CallbackQueryHandler(ds_button_callback, pattern='ds'))
app.add_handler(CallbackQueryHandler(ece_button_callback, pattern='ece'))
app.add_handler(CallbackQueryHandler(eie_button_callback, pattern='eie'))
app.add_handler(CallbackQueryHandler(eee_button_callback, pattern='eee'))
app.add_handler(CallbackQueryHandler(exit_button_callback, pattern='exit'))

app.add_handler(CallbackQueryHandler(admcse,pattern='admcse'))
app.add_handler(CallbackQueryHandler(admit,pattern='admit'))
app.add_handler(CallbackQueryHandler(admcs,pattern='admcs'))
app.add_handler(CallbackQueryHandler(admcsml,pattern='admcyberml'))
app.add_handler(CallbackQueryHandler(admds,pattern='admds'))
app.add_handler(CallbackQueryHandler(admece,pattern='admece'))
app.add_handler(CallbackQueryHandler(admeee,pattern='admeee'))
app.add_handler(CallbackQueryHandler(admcivil,pattern='admcivil'))
app.add_handler(CallbackQueryHandler(admmech,pattern='admmech'))

app.run_polling()