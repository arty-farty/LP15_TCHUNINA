"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    text1 = 'Для ввода названия планеты используйте "/planet [название планеты на англ]"'
    logging.info(text)
    update.message.reply_text(text)
    update.message.reply_text(text1)

def planet_user(bot, update):
    text = 'Для ввода названия планеты используйте "/planet [название планеты на англ]"'
    #planet = update.message.text.rsplit()
    planets=['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    user_input_planet=update.message.text[8:].capitalize()
    if user_input_planet in planets:
        d=datetime.datetime.now().strftime('%Y')
        if user_input_planet=='Sun':
            planet_answer=ephem.constellation(ephem.Sun(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer)
        elif user_input_planet=='Moon':
            planet_answer=ephem.constellation(ephem.Moon(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer)  
        elif user_input_planet=='Mercury':
            planet_answer=ephem.constellation(ephem.Mercury(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer)
        elif user_input_planet=='Venus':
            planet_answer=ephem.constellation(ephem.Venus(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer) 
        elif user_input_planet=='Mars':
            planet_answer=ephem.constellation(ephem.Mars(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer) 
        elif user_input_planet=='Jupiter':
            planet_answer=ephem.constellation(ephem.Jupiter(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer) 
        elif user_input_planet=='Saturn':
            planet_answer=ephem.constellation(ephem.Saturn(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer)  
        elif user_input_planet=='Uranus':
            planet_answer=ephem.constellation(ephem.Uranus(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer)  
        elif user_input_planet=='Neptune':
            planet_answer=ephem.constellation(ephem.Neptune(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer) 
        elif user_input_planet=='Pluto':
            planet_answer=ephem.constellation(ephem.Pluto(datetime.datetime.now().strftime('%Y')))
            bot.sendMessage(update.message.chat_id,planet_answer)
    else:
        planet_answer = "Неправильно введено название планеты"
        bot.sendMessage(update.message.chat_id,planet_answer)
#print(ephem.constellation(m))
    #constellation = ephem.constellation(planet)
    logging.info(text)
    #update.message.reply_text(planet_answer)

    #update.message.reply_text(text)
    #update.message.reply_text(constellation)
"""
def handle_status(msg):
    planet = update.message.text.split()
    constellation = ephem.constellation(planet)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                        update.message.chat.id,
                         update.message.text)
    update.message.reply_text(constellation)
"""
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    #, use_context=True)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_user))
    dp.add_handler(MessageHandler(Filters.text, planet_user))
    mybot.start_polling()
    mybot.idle()

main()      