import logging
# import requests
# from random import randint
# import json
# import os
# import random
# from reloading import reloading
from aiogram import Bot, Dispatcher, executor, types
# from test import link_nastya

import asyncio
from gpytranslate import Translator

# from datetime import date
# import time

# from subscription import add_sub, del_sub, get_subs


# from work_with_pdf import (
#     send_image,
#     download_and_create_pdf,
#     check,
#     create_file_members,
#     del_all_files,
#     create_today_name,
#     create_response,
#     post_request,
#     check_response,
#     uniqui_lines,
#     create_all_messages,
#     check_n,
# )
# from data import url, instructions, Members, config
# from PyPDF2 import PdfFileWriter, PdfFileReader
import openai
OPENAI_TOKEN = "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"  
import openai

bot = Bot(token="5339729956:AAGUE8dH1LERsBcrAdhgsYCTwzCK0OGgkEQ")

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
t = Translator()

# init openai
openai.api_key = OPENAI_TOKEN

@dp.message_handler(commands=["a"])
async def gpt_answer(message: types.Message):
    # await message.answer(message.text)

    model_engine = "text-davinci-003"
    max_tokens = 128  # default 1024
    prompt = await t.translate(message.text, targetlang="en")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt.text,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    await message.answer("ChatGPT: Генерирую ответ ...")
    translated_result = await t.translate(completion.choices[0].text, targetlang="ru")
    await message.answer(translated_result.text)


@dp.message_handler(commands=["all"])
async def call_all_users(message: types.Message):
    list_members = uniqui_lines(Members)

    my_message = create_all_messages(list_members)

    if message.chat.id == -1001786093308:
        await bot.send_message(message.chat.id, my_message)

if __name__ == "__main__":

    # asyncio.get_event_loop().create_task(pdf_check(url))
    executor.start_polling(dp, skip_updates=False)


# @dp.message_handler(commands=["to_all"])
# async def all_users(message: types.Message):
#     await message.answer(
#         f"{message.chat.id}  Привет, я бот для проверки наличия новых расписаний!"
#     )
#     try:
#         member = await bot.get_chat_member(message.chat.id, message.from_user.id)
#         create_file_members(member)
#         await message.answer(
#             f"{message.chat.id}  Привет, я бот для проверки наличия новых расписаний! А ты в базе!"
#         )
#     except TypeError:
#         await message.answer(f"{message.chat.id}  это не ваш чат")


# @dp.message_handler(commands=["sub"])
# async def all_users(message: types.Message):
#     if add_sub(message):
#         await message.answer("Вы подписаны на рассылку!")
#     else:
#         await message.answer("Вы уже подписаны на рассылку!")


# @dp.message_handler(commands=["fish"])
# async def all_users(message: types.Message):
#     random_num = random.randint(1, 15)
#     url = f'https://fish-text.ru/get?type=sentence&number={random_num}'
#     answer = requests.get(url).json()
#     print(answer)
#     await message.answer(answer['text'])
    


# @dp.message_handler(commands=["unsub"])
# async def all_users(message: types.Message):
#     del_sub(message)
#     await message.answer(f" Вы отписались от рассылки!")



# @dp.message_handler(commands="ras")
# async def ras(message: types.Message):

#     download_and_create_pdf(url)
#     today = create_today_name()
#     response = create_response()
#     check_response(response)
#     await send_image(bot, message)
#     del_all_files(today=today)
    
    
# @dp.message_handler(commands="for_nastya")
# async def ras(message: types.Message):
#     url1 = link_nastya()
#     download_and_create_pdf(url1)
#     today = create_today_name()
#     response = create_response()
#     check_response(response)
#     await send_image(bot, message)
#     del_all_files(today=today)



# @dp.message_handler(commands="r")
# async def ras(message: types.Message):
#     subs = get_subs()
#     # print(subs)
#     download_and_create_pdf(url)
#     today = create_today_name()
#     response = create_response()
#     check_response(response)
#     for sub in subs:
#         await send_image(bot, message=0, sub=sub)
#     del_all_files(today=today)


# @dp.message_handler(commands="help")
# async def answer(message: types.Message):
#     if message.chat.id == -1001786093308:
#         await bot.send_message(message.chat.id, "/help  \n /all \n /start ")
#     else:
#         await bot.send_message(message.chat.id, f"/ras \n  {message.chat.id}")


# async def pdf_check(url):
#     while True:
#         url_n = link_nastya()
        
#         pdf_n_1 = requests.get(url_n)
#         pdf = requests.get(url)
#         await asyncio.sleep(120)
#         time.sleep(2)
#         pdf_n_2 = requests.get(url_n)
#         pdf2 = requests.get(url)

#         with open("file_check_1.pdf", "wb") as file:
#             file.write(pdf.content)

#         with open("file_check_2.pdf", "wb") as file:
#             file.write(pdf2.content)
            
#         with open("n_1_file_check.pdf", "wb") as file:
#             file.write(pdf_n_1.content)

#         with open("n_2_file_check.pdf", "wb") as file:
#             file.write(pdf_n_2.content)
            
#         if check_n():
#             print("Н Again")
#             os.remove("n_1_file_check.pdf")
#             os.remove("n_2_file_check.pdf")
#         else:
#             url1 = link_nastya()
#             download_and_create_pdf(url1)
#             today = create_today_name()
#             response = create_response()
#             check_response(response)
#             await send_image(bot, message=1935061798)
#             del_all_files(today=today)
#         if check(url):
#             print("Again")
#             os.remove("file_check_1.pdf")
#             os.remove("file_check_2.pdf")
#             continue
#         else:
#             download_and_create_pdf(url)

#             response = create_response()

#             check_response(response)
#             await bot.send_message(-1001523814418, "Расписание пришло!\n /ras !")
#             await send_image(bot)
#             subs = get_subs()
#             today = create_today_name()

#             for sub in subs:
#                 await send_image(bot, message=0, sub=sub)
#             del_all_files(today=today)
#             await asyncio.sleep(120)


