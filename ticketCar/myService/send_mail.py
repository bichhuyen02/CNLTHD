from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pyrebase

from ticketCar.myService.firebase import firebase, auth

@csrf_exempt
def send_sms(request):

    # Lấy thông tin người nhận và nội dung tin nhắn từ request
    # phone_number = request.POST.get('phone_number')
    # message = request.POST.get('message')
    phone_number = '+84 386 858 149'
    message = 'message'

    # Gửi tin nhắn SMS
    user = auth.sign_in_with_email_and_password("tsanthibichhuyen@gmail.com", "khainguyenty21")
    user_id_token = user['idToken']
    messaging = firebase.messaging()
    response = messaging.send({
        "message": {
            "token": "210805",
            "data": {
                "phone_number": phone_number,
                "message": message
            },
            "android": {
                "data": {
                    "phone_number": phone_number,
                    "message": message
                }
            },
            "apns": {
                "payload": {
                    "aps": {
                        "content-available": True,
                        "mutable-content": True,
                        "alert": {
                            "title": "SMS Title",
                            "body": message
                        }
                    },
                    "custom": {
                        "phone_number": phone_number,
                        "message": message
                    }
                }
            }
        }
    }, user_id_token)

    return HttpResponse("SMS sent")