import datetime
import random
from rest_framework import status
from rest_framework.response import Response
from demo.sms import sendSMS
from rest_framework.views import APIView
from .models import OTP


class VerifyOTPView(APIView):
    def post(self, request):
        code = request.data.get("code")
        phone_number = request.data.get("phone_number")
        
        otp = OTP.objects.filter(code=code, phone_number=phone_number).first()

        if not otp:
            return Response("Invalid otp", status=status.HTTP_400_BAD_REQUEST)
        
        if otp.verified:
            return Response("otp already verified", status=status.HTTP_400_BAD_REQUEST)
        
        if datetime.datetime.now(tz=datetime.timezone.utc) > otp.created_at + datetime.timedelta(minutes=5):
            return Response("otp expired", status=status.HTTP_400_BAD_REQUEST)

        otp.verified = True
        otp.save()

        return Response("Successfully verified otp.", status=status.HTTP_200_OK)
       
    

    
class SendOTPView(APIView):
    def post(self, request):
        if "phone_number" not in request.data:
            return Response("phone_number is required", status=status.HTTP_400_BAD_REQUEST)
        
        code = random.randint(1000, 9999)
        phone_number = request.data["phone_number"]

        otp = OTP.objects.create(code=code, phone_number=phone_number)

        otp_message = f"Your OTP is {code}"
        
        sendSMS(phone_number, otp_message)

        return Response("Successfully sent the new otp", status=status.HTTP_200_OK)
            


