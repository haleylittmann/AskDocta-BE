from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Request, Doctor
from twilio.rest import Client

account_sid = os.environ['TWILIO_ID']
auth_token = os.environ['TWILIO_SECRET']
client = Client(account_sid, auth_token)
# Create your views here.

@csrf_exempt
def sms(request):
    if request.method == "POST":
        # Get the message the user sent our Twilio number
        body = request.POST.get('Body', "")
        number = request.POST.get('From', "")
        message = client.messages.create(
            body="Thank you for posting your request, a doctor should be in touch shortly!",
            from_="+19809490170",
            to=number
        )
        print(message.sid)
        Request.objects.create(message=body, phonenumber=number)
    else:
        return redirect('index')

def detail(request):
    return HttpResponse("%s" % request.message)
