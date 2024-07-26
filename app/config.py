import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    WHATSAPP_FROM = os.getenv('WHATSAPP_FROM')
    WHATSAPP_TO = os.getenv('WHATSAPP_TO')
