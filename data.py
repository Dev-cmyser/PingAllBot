from dotenv import dotenv_values
from typing import NamedTuple

config = dotenv_values(".env")  
url = config["URL"]

message = str
Link = str
Members = 'members.txt'

keys_pdf = ['pdf_live_MkqFIOoF2C9VBCtlovOixAkZN9th1Vqn452qJyD91Ug','pdf_live_9vfydSfsNtwzPXQILUzAFL4nFG4745HT1CV4diOtfj1']



# class Data(NamedTuple):
#     """
#     Data class for the data.
#     """
#     data: str
#     label: str
    
instructions = {
                "parts": [{"file": "document"}],
                "output": {"type": "image", "format": "png", "dpi": 300},
            }