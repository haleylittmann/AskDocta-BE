from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Request, Doctor, Patient
from twilio.rest import Client
from django.shortcuts import redirect
from .forms import UserForm
from .forms import DoctorForm
from .forms import PatientForm
import os

account_sid = os.environ['TWILIO_ID']
auth_token = os.environ['TWILIO_SECRET']
client = Client(account_sid, auth_token)
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.doctor.phone:
        return redirect('/profile/edit')
    return render(request, 'index.html')

def patient(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.doctor.phone:
        return redirect('/profile/edit')
    patients = Patient.objects.all()
    return render(request, 'patient/index.html', {'patients': patients})

def detail(request, request_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.doctor.phone:
        return redirect('/profile/edit')
    try:
        r = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        raise Http404("Request does not exist")
    if request.method == "POST":
        delVal = request.POST.get('delete')
        if delVal:
            message = client.messages.create(
                body="A Doctor has accepted your request, expect a text from them soon.",
                from_="+19809490170",
                to=r.phonenumber
            )
            print(message.sid)
            message2 = client.messages.create(
                body="You've approved the patient request, please contact them at %s" %r.phonenumber,
                from_="+19809490170",
                to=str(request.user.doctor.phone)
            )
            print(message2.sid)
            r.delete()
            return redirect('index')
        else:
            return redirect('index')
            # return render(request, 'request/detail.html', {'request': r})
    else:
        return render(request, 'request/detail.html', {'request': r})

def new_patient(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        patient_form = PatientForm()
    return render(request, 'patient/new.html', {
        'patient_form': patient_form,
    })

def patient_detail(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.doctor.phone:
        return redirect('/profile/edit')
    try:
        p = Patient.objects.get(id=request_id)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return render(request, 'patient/detail.html', {'request': p})

def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        doctor_form = DoctorForm(request.POST, instance=request.user.doctor)
        if user_form.is_valid() and doctor_form.is_valid():
            user_form.save()
            doctor_form.save()
            return redirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        doctor_form = DoctorForm(instance=request.user.doctor)
    return render(request, 'profiles/edit.html', {
        'user_form': user_form,
        'doctor_form': doctor_form
    })


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