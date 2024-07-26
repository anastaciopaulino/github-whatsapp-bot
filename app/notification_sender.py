import requests
from .config import Config

class NotificationSender:
    def __init__(self):
        self.auth_token = Config.TWILIO_AUTH_TOKEN
        self.account_sid = Config.TWILIO_ACCOUNT_SID
        self.whatsapp_from = Config.WHATSAPP_FROM
        self.whatsapp_to = Config.WHATSAPP_TO
    
    def send_whatsapp_message(self, message):
        url = f'https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/Messages.json'
        data = {
            'From': self.whatsapp_from,
            'To': self.whatsapp_to,
            'Body': message
        }
        response = requests.post(url, data=data, auth=(self.account_sid, self.auth_token))
        response.raise_for_status()
        return response
