from django.db import models

class OTP(models.Model):
    phone_number = models.CharField(max_length=10)
    code = models.CharField(max_length=6, null=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    verified = models.BooleanField(default = False)
