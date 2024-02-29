from django.conf import settings
from twilio.rest import Client

TWILIO_ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
TWILIO_MSG_SERVICE_SID = settings.TWILIO_MSG_SERVICE_SID

def sendSMS(phoneNumber, message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(body="{}".format(message), to=phoneNumber, messaging_service_sid=TWILIO_MSG_SERVICE_SID)
        # return message
    except Exception as e:
        raise Exception("Cant send sms")