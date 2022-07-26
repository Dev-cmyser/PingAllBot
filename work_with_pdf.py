import asyncio
import requests
import json
import os
from datetime import date
from data import Link, message, instructions, keys_pdf
from aiogram import types
from PyPDF2 import PdfFileWriter, PdfFileReader

def check_n() -> bool:
    
    with open("n_1_file_check.pdf", "rb") as file_1:
        with open("n_2_file_check.pdf", "rb") as file_2:

            if file_1.read() == file_2.read():
                return True
            else:
                return False


def check(url: Link) -> bool:

    with open("file_check_1.pdf", "rb") as file_1:
        with open("file_check_2.pdf", "rb") as file_2:

            if file_1.read() == file_2.read():
                return True
            else:
                return False


def uniqui_lines(filename: str) -> list:
    with open(f"{filename}", "r") as file:
        uniqui_lines = set(file.readlines())
    return uniqui_lines


def create_file_members(member: types.ChatMember) -> None:
    with open("members.txt", "a") as file:
        member_name = "@" + member.user.username
        file.write(member_name + "\n")


def download_and_create_pdf(url: Link) -> None:
    pdf = requests.get(url)
    
    with open("spo.pdf", "wb") as file:
        file.write(pdf.content)


def create_all_messages(list_members: list) -> message:
    my_message = ""
    for message in list_members:
        my_message += message + "\n"
    return my_message


def parse_pdf_on_pages(input_PDF: PdfFileReader) -> None:
    for i in range(input_PDF.getNumPages()):
        output = PdfFileWriter()
        new_File_PDF = input_PDF.getPage(i)
        output.addPage(new_File_PDF)
        output_Name_File = "spo" + str(i + 1) + ".pdf"
        outputStream = open(output_Name_File, "wb")
        output.write(outputStream)
        outputStream.close()



def post_request(page_count=0, key=0) -> requests.Response:
    if page_count:
        return requests.request(
        "POST",
        "https://api.pspdfkit.com/build",
        headers={
            "Authorization": f"Bearer {keys_pdf[key]}"
        },
        files={"document": open(f"spo{page_count}.pdf", "rb")},
        data={"instructions": json.dumps(instructions)},
        stream=True,
    )
        
    else:
        
        return requests.request(
        "POST",
        "https://api.pspdfkit.com/build",
        headers={
            "Authorization": f"Bearer {keys_pdf[key]}"
        },
        files={"document": open(f"spo.pdf", "rb")},
        data={"instructions": json.dumps(instructions)},
        stream=True,
    )
        


def create_today_name() -> str:
    today = date.today()
    today = str(today)[5:]
    today += ".png"
    return today


def create_image(today: str, response, count='0') -> None:
    
    if isinstance(response, list):
        for r in response:
            name = count + today
            count += '1'
            with open(name, "wb") as image:
                for chunk in r.iter_content(chunk_size=8096):
                    image.write(chunk)
    else:
        with open(today, "wb") as image:
            for chunk in response.iter_content(chunk_size=8096):
                image.write(chunk)
    
    # with open(f"{count}", "wb") as image:
    #     for chunk in response.iter_content(chunk_size=8096):
    #         image.write(chunk)


def check_response(response: requests.Response) -> None:
    today = create_today_name()
    if isinstance(response, list):
        
        if response[0].ok:
            create_image(today, response=response)
            
            
        else:
            print(response[0].text)
        
    else:
        if response.ok:
            create_image(today, response=response)
        else:
            print(response.text)
            

async def send_image(bot, message=0, sub=0) -> None:
    # for response in create_response():
    today = create_today_name()
    
    await send_real(bot=bot, message=message, sub=sub, today=today)


        
            
            
            
async def send_real(bot, message=0, sub=0, today='') -> None:
    if os.path.isfile(f"0{today}") and os.path.isfile(f"01{today}"):
        if message == 1935061798:
            await bot.send_photo(1935061798, photo=open(f"0{today}", "rb"))
            await bot.send_photo(1935061798, photo=open(f"01{today}", "rb"))
        if message:
            if message.chat.id:
                await bot.send_photo(message.chat.id, photo=open(f"0{today}", "rb"))
                await bot.send_photo(message.chat.id, photo=open(f"01{today}", "rb"))
        else:
            if sub:
                await bot.send_photo(sub, photo=open(f"0{today}", "rb"))
                await bot.send_photo(sub, photo=open(f"01{today}", "rb"))
            else:
                await bot.send_photo(-1001523814418, photo=open(f"0{today}", "rb"))
                await bot.send_photo(-1001523814418, photo=open(f"01{today}", "rb"))
                await bot.send_photo(762133897, photo=open(f"0{today}", "rb"))
                await bot.send_photo(762133897, photo=open(f"01{today}", "rb"))
    else:
        if message == 1935061798:
            await bot.send_photo(1935061798, photo=open(f"0{today}", "rb"))
            await bot.send_photo(1935061798, photo=open(f"01{today}", "rb"))
        if message:
            if message.chat.id:
                await bot.send_photo(message.chat.id, photo=open(today, "rb"))
        else:
            if sub:
                await bot.send_photo(sub, photo=open(today, "rb"))
            else:
                await bot.send_photo(-1001523814418, photo=open(today, "rb"))
                await bot.send_photo(762133897, photo=open(today, "rb"))
        


def del_all_files(today: str) -> None:
    if os.path.isfile(today):
        os.remove(today)
    if os.path.isfile("spo.pdf"):
        os.remove("spo.pdf")
    if os.path.isfile("spo1.pdf"):
        os.remove("spo1.pdf")
    if os.path.isfile("spo2.pdf"):
        os.remove("spo2.pdf")
    if os.path.isfile(f"0{today}"):
        os.remove(f'0{today}')
    if os.path.isfile(f"01{today}"):
        os.remove(f'01{today}')
        
        
        
def create_response() -> requests.Response:
    
    with open("spo.pdf", "rb") as f:

        input_PDF = PdfFileReader(f)
        parse_pdf_on_pages(input_PDF)

        if input_PDF.getNumPages() > 1:

            parse_pdf_on_pages(input_PDF)

            page_count = 1
            responses = []
            key = 0
            for i in range(input_PDF.getNumPages()):
                
                response = post_request(page_count=page_count)
                print('\n')
                print(response)
                print('\n')
                if type(response) == dict:
                    key += 1
                    response = post_request(page_count=page_count, key=key)
                page_count += 1
                
                responses.append(response)
            return responses
                
        else:
    
            response = post_request()
            return response