
import telebot

bot = telebot.TeleBot("6944267196:AAGP8BvpQNcH-ezMzB2alY8BboHrM0KMzCI")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()