import telebot
from telebot import types

# Укажите ваш токен здесь
TOKEN = '7349866755:AAFxYLj3FiN538wW63W6AkCj76B5hyNzrVk'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Click Me!", url="https://uh0hhp.onrender.com/clicker")
    keyboard.add(url_button)
    
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Choose an action:", reply_markup=keyboard)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    # Пример обработчика для текстовых сообщений
    bot.send_message(message.chat.id, "I don't understand this command.")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
