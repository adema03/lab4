# This Python file uses the following encoding: utf-8
import telebot
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
TOKEN = "6919349415:AAEXnYZok_C4vN6wydBrsr57N48MX4X91v0"
rpc_user = 'kzcashrpc'
rpc_password = '4p70VpuvDKwWv4yI2fbZfaRr'

rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@127.0.0.1:8276')

bot = telebot.TeleBot(TOKEN)

# старт
@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Привет")
# Обработчик команды getnewaddress
@bot.message_handler(commands=['getnewaddress'])
def get_new_address(message):
    new_address = rpc_connection.getnewaddress()
    bot.reply_to(message, f"Новый адрес кошелька: {new_address}")

# Обработчик команды getbalance
@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    balance = float(rpc_connection.getbalance())
    bot.reply_to(message, f"Баланс кошелька: {balance}")

# echo bot
@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()