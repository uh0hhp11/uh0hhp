from flask import Flask, request, jsonify
import telebot

# Укажите токен вашего бота здесь
TOKEN = '7349866755:AAFxYLj3FiN538wW63W6AkCj76B5hyNzrVk'

# Устанавливаем Webhook URL
WEBHOOK_URL = 'https://uh0hhp.onrender.com/webhook'  # Замените на ваш реальный домен

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Маршрут для установки Webhook
@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    if request.method == 'POST':
        bot.remove_webhook()
        s = bot.set_webhook(url=WEBHOOK_URL)
        if s:
            return "Webhook setup successful!"
        else:
            return "Failed to set webhook."
    else:
        return "Method not allowed."

# Маршрут для обработки POST-запросов на /webhook
@app.route('/webhook', methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return jsonify({'status': 'ok'})
    else:
        return "Method not allowed."

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(text="Click Me!", url="https://uh0hhp.onrender.com/clicker")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Welcome to the Clicker WebApp!", reply_markup=keyboard)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
