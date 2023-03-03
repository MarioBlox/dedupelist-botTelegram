import telebot

bot = telebot.TeleBot('BOTTOKEN')

@bot.message_handler(content_types=['text'])
def handle_message(message):
    lines = message.text.split('\n')
    unique_lines = list(set(lines))
    response_text = '\n'.join(unique_lines)
    bot.send_message(message.chat.id, response_text)

bot.polling()
