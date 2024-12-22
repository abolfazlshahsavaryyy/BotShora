import telebot
import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = str(os.getenv("TOKEN"))
bot = telebot.TeleBot(BOT_TOKEN)

USER_CHAT_ID = int(os.getenv("ABOLFAZL_ID"))


user_states = {}

@bot.message_handler(commands=['start'])
def start_command_handler(message):
    user_id = message.chat.id
    bot.send_message(user_id, "سلام بر دانشجوی دانشگاه علم و صنعت مهندسی کامپیوتر لطفا پیام خود را ارسال کنید.")
    user_states[user_id] = "waiting_for_message"

@bot.message_handler(func=lambda message: True)
def handle_user_message(message):
    user_id = message.chat.id
    
    
    if user_states.get(user_id) == "waiting_for_message":
        try:
           
            messageToSend=message.text
            messageToSend+="\n"
            messageToSend+="#ارسالی"
            bot.send_message(chat_id=USER_CHAT_ID, text=messageToSend)
            
            bot.send_message(user_id, "پیام شما برای شورای صنفی ارسال شد ممنون از همکاری شما.")
        except Exception as e:
            bot.send_message(user_id, f"Failed to send the message")
        
        
        user_states[user_id] = None
    else:
        
        bot.send_message(user_id, "Please use /start to begin.")


bot.polling()
