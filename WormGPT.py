from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
import requests
import telebot
import sqlite3
import html
import json
import os
import re
import urllib3
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
elsfahelmsry = '8539569852:AAGTnvFQc_CdQtW_Ycoe30eKgqMvLHby6VM'
ADMIN = '5960722875'
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
zo = telebot.TeleBot(elsfahelmsry)
conn = sqlite3.connect('channels.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS channels (id INTEGER PRIMARY KEY, channel_name TEXT, invite_link TEXT)''')
data = {}
current_messages = {}
current_message_index = {}
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists('data/data.json'):
    with open('data/data.json', 'w') as f:
        json.dump({}, f)
with open('data/data.json', 'r') as f:
    try:
        data = json.load(f)
    except:
        data = {}
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
@zo.callback_query_handler(func=lambda call: call.data == 'Back')
def show_settings(call):
    markup = types.InlineKeyboardMarkup(row_width=2)

    user = zo.get_chat(call.from_user.id)
    owner_name = user.first_name
    owner_link = f"[{owner_name}](tg://user?id={call.from_user.id})"

    k_add = types.InlineKeyboardButton('➕ إضافة قناة', callback_data='add_channel')
    k_remove = types.InlineKeyboardButton('➖ حذف قناة', callback_data='remove_channel')
    k_show = types.InlineKeyboardButton('🗂 قائمة القنوات', callback_data='show_channels')
    k_delete_all = types.InlineKeyboardButton('🗑️ حذف جميع القنوات', callback_data='delete_all_channels')
    markup.add(k_show)
    markup.add(k_add, k_remove)
    markup.add(k_delete_all)
    
    zo.edit_message_text(
        chat_id=call.message.chat.id, 
        message_id=call.message.message_id,
        text=f'👤 *لوحة الأدمن*:\n\n👑 مرحباً {owner_link} في اللوحة الخاصة بك:',
        reply_markup=markup, 
        parse_mode='Markdown'
    )
    zo.clear_step_handler(call.message
    )
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
def subscs(user_id):
    channels = cursor.execute("SELECT channel_name, invite_link FROM channels").fetchall()
    for channel in channels:
        channel_username, invite_link = channel
        try:
            member_status = zo.get_chat_member(chat_id=channel_username, user_id=user_id).status
            if member_status not in ["member", "administrator", "creator"]:
                return False, invite_link
        except Exception as e:
            continue
    return True, None
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
def not_subscrip(message, invite_link):
    na = message.from_user.first_name
    if invite_link:
        channel_url = invite_link.replace('@', '')
        button = telebot.types.InlineKeyboardMarkup(row_width=1)
        subscribe_button = telebot.types.InlineKeyboardButton(text="اشترك", url=f"{channel_url}")
        button.add(subscribe_button)
        zo.reply_to(
            message, 
            text=f'''
• Welcome! Before using the bot:
• {invite_link}
• Subscribe to the channel to get updates.
• Then come back and send /start.
''',
            disable_web_page_preview=True,
            reply_markup=button
        )
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
def not_subscrip1(call, invite_link):
    na = call.from_user.first_name
    if invite_link:
        channel_url = invite_link.replace('@', '')
        button = telebot.types.InlineKeyboardMarkup(row_width=1)
        subscribe_button = telebot.types.InlineKeyboardButton(text="اشترك", url=f"{channel_url}")
        button.add(subscribe_button)
        zo.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id, 
            text=f'''
• Welcome! Before using the bot:
• {invite_link}
• Subscribe to the channel to get updates.
• Then come back and send /start.
''',
            disable_web_page_preview=True,
            reply_markup=button
        )
        zo.clear_step_handler(call.message)

#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
@zo.message_handler(commands=['start'])
def vip1(message):
    is_subscribed, channel = subscs(message.from_user.id)
    if not is_subscribed:
        not_subscrip(message, channel)
        return

    ph2 = 'https://t.me/Z_O_Z_0o0/2'
    text = '''
<b>Hi Too User :)</b>
<blockquote><tg-spoiler>⚠️ Disclaimer:
This project was created for educational and research purposes only, and I bear no responsibility for any misuse or illegal activities carried out using this tool. The user is solely responsible for how they choose to use it. ‼️</tg-spoiler></blockquote>

<b>Speak...</b>'''
    
    zo.send_photo(
        chat_id=message.chat.id,
        photo=ph2,
        caption=text,
        parse_mode='HTML',
        reply_to_message_id=message.message_id
    )
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
@zo.message_handler(commands=['admin'])
def admin_command(message):
    user_id = message.from_user.id
    if user_id in ADMIN:
    	markup = types.InlineKeyboardMarkup(row_width=2)
    	
    	user = zo.get_chat(message.from_user.id)
    	owner_name = user.first_name
    	owner_link = f"[{owner_name}](tg://user?id={message.from_user.id})"
    	k_add = types.InlineKeyboardButton('➕ إضافة قناة', callback_data='add_channel')
    	k_remove = types.InlineKeyboardButton('➖ حذف قناة', callback_data='remove_channel')
    	k_show = types.InlineKeyboardButton('🗂 قائمة القنوات', callback_data='show_channels')
    	k_delete_all = types.InlineKeyboardButton('🗑️ حذف جميع القنوات', callback_data='delete_all_channels')
    	markup.add(k_show)
    	markup.add(k_add, k_remove)
    	markup.add(k_delete_all)
    	zo.reply_to(
                message, 
                text=f'👤 *لوحة الأدمن*:\n\n👑 مرحباً {owner_link} في اللوحة الخاصة بك:',
            reply_markup=markup, 
            parse_mode='Markdown'
)
   
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
import webbrowser
webbrowser.open('https://t.me/elsfahelmsry')

@zo.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
    markup.add(back_button)

    if call.data == 'add_channel':
        add_text = '🔹 قم بإرسال يوزر القناة بـ(@) لإضافتها :'
        zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=add_text, reply_markup=markup)
        zo.register_next_step_handler(call.message, add_channel)

    elif call.data == 'remove_channel':
        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
        markup.add(back_button)
        delete_text = '🔸 قم بإرسال يوزر القناة بـ(@) لحذفها :'
        zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=delete_text,reply_markup=markup)
        zo.register_next_step_handler(call.message, remove_channel)

#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
    elif call.data == 'delete_all_channels':
        confirmation_markup = types.InlineKeyboardMarkup()
        confirm_button = types.InlineKeyboardButton("✔️ | تأكيد الحذف | ✔️", callback_data='confirm_delete_all')
        cancel_button = types.InlineKeyboardButton("❌ | تراجع | ❌", callback_data='cancel_delete')
        confirmation_markup.add(confirm_button, cancel_button)

        confirmation_text = '''
⚠️ | *هل أنت متأكد أنك تريد حذف جميع القنوات والمجموعات؟*
✨ | *ستتم عملية الحذف بشكل نهائي*
'''
        zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=confirmation_text, parse_mode='Markdown', reply_markup=confirmation_markup)
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
    elif call.data == 'confirm_delete_all':
        cursor.execute('SELECT channel_name FROM channels')
        channels = cursor.fetchall()

        if channels:
            deletes_text = '''
👑 | عزيزي المالك 😊❤️
✔️ | *تم حذف جميع القنوات بنجاح*

🗑️ | *القنوات المحذوفة :*
د— — — — — — — — — — —
'''
            for channel in channels:
                deletes_text += f'👉 | {channel[0]}\n'
            deletes_text += 'د— — — — — — — — — — —'

            cursor.execute('DELETE FROM channels')
            conn.commit()
            zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=deletes_text, parse_mode='Markdown', reply_markup=markup)

        else:
            erer_deletes_text = '''
⚠️ | عزيزي المالك 🌚❤️
❌ | *لا توجد قنوات لحذفها*
د— — — — — — — — — — —
'''
            zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=erer_deletes_text, parse_mode='Markdown', reply_markup=markup)
    elif call.data == 'cancel_delete':
        cancel_text = '😮‍💨 | *تم إلغاء عملية الحذف* | 😮‍💨'
        zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=cancel_text, parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'show_channels':
        cursor.execute("SELECT channel_name FROM channels")
        channels = cursor.fetchall()
        markup = types.InlineKeyboardMarkup()
        if channels:
            show_text = '📋 قنوات الاشتراك الإجباري :'
            for channel in channels:
                channel_name = channel[0].replace("@", "")
                button = types.InlineKeyboardButton(
                    text=f'🔹 {channel_name}',
                    url=f'https://t.me/{channel_name}'
                )
                markup.add(button)
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            markup.add(Back)
            zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=show_text, reply_markup=markup)
        else:
            not_exist_text = '❌ ¦ لا توجد قنوات مسجله حاليا ¦ ❌'
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            markup.add(Back)

            zo.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=not_exist_text, reply_markup=markup)
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
def add_channel(message):
    channel_name = message.text.strip()
    if not channel_name.startswith('@'):
        channel_name = '@' + channel_name
    try:
        chat_info = zo.get_chat(channel_name)
        if chat_info.type not in ['channel', 'supergroup', 'group']:
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            markup.add(Back)
            text = '❌ ¦ يجب أن يكون اليوزر قناة أو مجموعة ¦ ❌'
            zo.reply_to(message, text=text, reply_markup=markup, parse_mode='Markdown')
            return
        
        chat_members = zo.get_chat_administrators(channel_name)
        bot_is_admin = any(member.user.id == zo.get_me().id for member in chat_members)

        if not bot_is_admin:
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            markup.add(Back)
            text = '🚫 ¦ يجب أن يكون البوت أدمن في القناة أو المجموعة  ¦ 🚫'
            zo.reply_to(message, text=text, reply_markup=markup, parse_mode='Markdown')
            return

        cursor.execute("SELECT * FROM channels WHERE channel_name = ?", (channel_name,))
        channel = cursor.fetchone()

        if channel:
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            Zo_text = f'''
            👑 | عزيزي المالك 😢💔
❌ | القناة موجودة بالفعل 
د— — — — — — — — — — —
د - {channel_name}
د— — — — — — — — — — —
'''
            markup.add(Back)
            zo.reply_to(message, Zo_text, reply_markup=markup)
        else:
            invite_link = zo.export_chat_invite_link(chat_info.id)
            cursor.execute("INSERT INTO channels (channel_name, invite_link) VALUES (?, ?)",
                       (channel_name, invite_link))
            conn.commit()
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            Zo_text = f'''
            👑 | عزيزي المالك 😊❤️
✔ | تم إضافة القناة بنجاح 
د— — — — — — — — — — —
د - {channel_name}
🔗 | رابط الدعوة: {invite_link}
د— — — — — — — — — — —
'''
            markup.add(Back)
            zo.reply_to(message, Zo_text, reply_markup=markup)

    except telebot.apihelper.ApiException as e:
        if "chat not found" in e.description:
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            markup.add(Back)
            text = '❌ ¦ اسم القناة أو المجموعة غير صحيح ¦ ❌'
            zo.reply_to(message, text=text, reply_markup=markup, parse_mode='Markdown')
        elif "Forbidden: bot was kicked" in e.description:
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            markup.add(Back)
            text = '🚫 ¦ البوت محظور من المجموعة أو القناة ¦ 🚫'
            zo.reply_to(message, text=text, reply_markup=markup, parse_mode='Markdown')
        else:
            zo.reply_to(message, f'خطأ: {e.description}')
    except Exception as e:
        text = f"حدث خطأ: {str(e)}"
        markup = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
        markup.add(Back)
        zo.reply_to(message, text=text, reply_markup=markup, parse_mode='Markdown')
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
def remove_channel(message):
    channel_name = message.text.strip()
    
    with sqlite3.connect('channels.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM channels WHERE channel_name = ?", (channel_name,))
        channel = cursor.fetchone()
        
        if channel:
            cursor.execute("DELETE FROM channels WHERE channel_name = ?", (channel_name,))
            conn.commit()
            
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            Zo_text = f'''
👑 | عزيزي المالك 😢💔
✔ | تم حذف القناة بنجاح 
د— — — — — — — — — — —
د - {channel_name}
د— — — — — — — — — — —
            '''
            markup.add(Back)
            zo.send_message(
                message.chat.id,
                text=Zo_text,
                reply_markup=markup
            )
        else:
            markup = types.InlineKeyboardMarkup()
            Back = types.InlineKeyboardButton("• رجوع •", callback_data='Back')
            Zo_text = f'''
👑 | عزيزي المالك 🌚❤️
❌ | القناة غير موجودة لحذفها 
د— — — — — — — — — — —
د - {channel_name}
د— — — — — — — — — — —
            '''
            markup.add(Back)
            zo.send_message(
                message.chat.id,
                text=Zo_text,
                reply_markup=markup
            )
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
@zo.message_handler(func=lambda message: True)
def vip2(message):
    is_subscribed, channel = subscs(message.from_user.id)
    if not is_subscribed:
        not_subscrip(message, channel)
        return
    e1 = message.text
    zo.send_chat_action(message.chat.id, 'typing')
    try:
        req = requests.post(
            "https://sii3.top/api/error/wormgpt.php",
            data={
                'key': "DarkAI-WormGPT-E487DD2FDAAEDC31A56A8A84",
                'text': e1
            }
        )

        if req.status_code == 200:
            reda = req.json()
            if "response" in reda:
                repbot = reda["response"]
                if len(repbot) > 4000:
                    for i in range(0, len(repbot), 4000):
                        zo.send_message(message.chat.id, repbot[i:i+4000])
                else:
                    zo.reply_to(message, repbot)
            else:
                zo.reply_to(message, "*• عذرا حدث خطاء ما تواصل مع المطور 😊✨*", parse_mode='Markdown')
        else:
            zo.reply_to(message, "*• عذرا حدث خطاء ما تواصل مع المطور 😊✨ً*")
    except json.JSONDecodeError:
        zo.reply_to(message, "*• عذرا حدث خطاء ما تواصل مع المطور 😊✨ٌ*", parse_mode='Markdown')
#غير الحقوق واثبت انك فاشل اذا تريد تنقل اذكر اسمي او اسم قناتي #

#====================#
#CH : @elsfahelmsry 
#DEV : @ELSFAH111
#====================#
print("🖤 لا تيأس حاول حتى يعمل 🖤")
zo.delete_webhook()
zo.infinity_polling()