from datetime import datetime
import time
import json
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types


# Конфиг для бота
file = open('config.json', 'r')
config = json.load(file)
#

# Мишура
MSG = 'Ты кодил седня хоть?'
#

# Подключение бота непосредственно
bot = Bot(token=config['TOKEN'])
dp = Dispatcher(bot=bot)
#

# Отслеживание сообщения старта 
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {datetime.now()}')
    if user_full_name == 'sensed':                                                                           #  Если это мой юзернейм:
        await message.reply(f"Привет, хозяин, сейчас {datetime.now().hour}:{datetime.now().minute}!")       #  он будет обращаться ко мне как хозяин и писать время (Ч:М)
    else:                                                                                                    #  Иначе:
        await message.reply(f"Привет, {user_full_name}")                                                     #  по полному нику в телеграме

    while True:                                                                  #   Бесконечный цикл который надо пофиксить
        datetime.now()                                                           #   проверка времени сейчас
        if (datetime.now().hour > 7) and (datetime.now().hour < 23):             #   если время сейчас в промежутке 8-22
            await bot.send_message(user_id, MSG.format(user_name))               #   то спросить MSG

        await asyncio.sleep(60*60)                                               #   спим час и цикл по новой
#


# ООП мишура
if __name__ == "__main__":
    executor.start_polling(dp)
#