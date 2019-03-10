from django.shortcuts import render

# Create your views here.

def sms(request):
    if request.method == "POST":
        # Get the message the user sent our Twilio number
        body = request.values.get('Body', None)
        resp = MessagingResponse()
        resp.message("Thank you for posting your request, a doctor should be in touch shortly!")
        Request.objects.create(message = body)
        return str(resp)
    else:
        return redirect('index')

def detail(request):
    return HttpResponse("%s" % request.message)