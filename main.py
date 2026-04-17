import os
from flask import Flask, request
import telegram

app = Flask(__name__)
TOKEN = os.environ.get('BOT_TOKEN')
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def home():
    return 'Bot vivo'

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id=chat_id, text='Bot activo bb. Tira el comando que quieras ❤️')
    return 'ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
