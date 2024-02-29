from django.contrib import admin
from django.urls import path, include

from demo import views


urlpatterns = [
     path('send-otp/', views.SendOTPView.as_view(), name='send_otp'),
     path('verify-otp/', views.VerifyOTPView.as_view(), name='verify_otp'),
     path('admin/', admin.site.urls),
]

