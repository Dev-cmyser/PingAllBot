from aiogram import types
import os


def add_sub(message: types.Message) -> bool:
    with open('sub.txt', "r") as f:
        subs = f.readlines()
        
        if (str(message.chat.id)+"\n") not in subs:
            with open('sub.txt', "a") as file:
                file.write(str(message.chat.id) + "\n")
                return True
        else:
            return False
        
def del_sub(message: types.Message) -> None:
    
    with open('sub.txt', "r") as f:
        lines = f.readlines()
    
    os.remove('sub.txt')
    if (str(message.chat.id)+"\n") in lines:
        print(lines)
        lines.remove(str(message.chat.id) + "\n")
        try:
            lines.remove("\n")
        except ValueError:
            pass
    with open('sub.txt', "w") as f:
        for line in lines:
            f.write(line)
            
            
def get_subs() -> list:
    with open('sub.txt', "r") as f:
        lines = f.readlines()
    return lines