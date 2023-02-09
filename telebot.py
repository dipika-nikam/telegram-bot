import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token='6017829834:AAGEymk5mWsquk742-0qySomdyJg-UuHZpk', use_context=True)

def start(update, context):
    message = "Transforming Your Digital Presence, Beautifully 💻👩‍💼✨"
    message += "<b><a href='https://infynno.com/'>Infynno Solutions</a></b> \n\n"
    message += "Our focus is on supporting the growth and expansion of SaaS startups through our expertise in web and mobile app development."
    buttons = [
        telegram.InlineKeyboardButton("Portfolio 🗂️", callback_data='option_1', url='https://infynno.com/portfolios/'),
        telegram.InlineKeyboardButton("Services 💼", callback_data='option_2'),
        telegram.InlineKeyboardButton("Company 💻", callback_data='option_3'),
        telegram.InlineKeyboardButton("Career 🏆", url='https://infynno.com/career/', callback_data='option_4'),
        telegram.InlineKeyboardButton("Contact us 📲", callback_data='option_5', url='https://infynno.com/get-a-quote/')
    ]
    reply_markup = telegram.InlineKeyboardMarkup(build_menu(buttons, n_cols=2))
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('image 2.png', 'rb'), caption=message, reply_markup=reply_markup, parse_mode=telegram.ParseMode.HTML)

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def hi(update, context):
    if update.message.text == '/start':
        start(update, context)
    elif update.message.text == 'thank you' or update.message.text == 'Thank you':
        context.bot.send_message(chat_id=update.message.chat_id, text="Happy to help! 😄")
    elif update.message.text =='bye' or  update.message.text =='Bye' or  update.message.text =='by' or update.message.text =='By':
        context.bot.send_message(chat_id=update.message.chat_id, text="Take care! Hope to talk to you again soon.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Connect with us now for any assistance. Thanks!")

def button(update, context):
    query = update.callback_query
    context.bot.answer_callback_query(query.id)
    if query.data == 'option_2':
        if update.callback_query:
            chat_id = update.callback_query.message.chat_id
            button_list = [
                [telegram.InlineKeyboardButton(f"Web Development", url='https://infynno.com/service/web-development/',callback_data="1_1"),
                telegram.InlineKeyboardButton("Mobile Development", url='https://infynno.com/service/nodejs-development/', callback_data="1_2")],
                [telegram.InlineKeyboardButton("ReactJs", url='https://infynno.com/service/reactjs-development/', callback_data="2_1"),
                telegram.InlineKeyboardButton("Laravel", url='https://infynno.com/service/laravel-development/',  callback_data="2_2")],
                [telegram.InlineKeyboardButton("React Native", url='https://infynno.com/service/react-native-development/',  callback_data="2_1"),
                telegram.InlineKeyboardButton("Creative Designs",url='https://infynno.com/service/creative-designs/', callback_data="2_2")],
                [telegram.InlineKeyboardButton("Cloud Services",url='https://infynno.com/service/cloud-services/', callback_data="2_1")],
            ]
            reply_markup = telegram.InlineKeyboardMarkup(button_list)
            context.bot.send_photo(chat_id=chat_id, photo=open('8263.jpg_wh300.jpg', 'rb'), caption="Services 💼", reply_markup=reply_markup, parse_mode=telegram.ParseMode.HTML)
        else:
            print('hey')
   
    if query.data == 'option_3':
        if update.callback_query:
            chat_id = update.callback_query.message.chat_id
            button_list = [
                [telegram.InlineKeyboardButton("About us ", url='https://infynno.com/about-us/', callback_data="2_2"),
                telegram.InlineKeyboardButton(f"Our Team", url='https://infynno.com/team/',callback_data="2_1")],
                [telegram.InlineKeyboardButton("Life at Infynno", url='https://infynno.com/celebrations/',  callback_data="2_2")],
            ]
            reply_markup = telegram.InlineKeyboardMarkup(button_list)

            context.bot.send_photo(chat_id=chat_id, photo=open('company.png', 'rb'), caption="Company 💻", reply_markup=reply_markup, parse_mode=telegram.ParseMode.HTML)
            
        else:
            print('hey')           

    if query.data == 'option_7':
        if update.callback_query:
            chat_id = update.callback_query.message.chat_id
            context.bot.send_message(chat_id=chat_id, text="Nice to meet you")


hi_handler = MessageHandler(Filters.text, hi)
button_handler = CallbackQueryHandler(button)

updater.dispatcher.add_handler(hi_handler)
updater.dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()