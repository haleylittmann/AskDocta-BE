from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Profile, Patient
from twilio.rest import Client
from django.shortcuts import redirect
from .forms import UserForm
from .forms import ProfileForm
from .forms import PatientForm
from .forms import SortForm
from .forms import PermissionsForm
from django.contrib import messages
from django.template.defaulttags import register
import os

account_sid = os.environ['TWILIO_ID']
auth_token = os.environ['TWILIO_SECRET']
client = Client(account_sid, auth_token)
# Create your views here.
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.profile.phone:
        return redirect('/profile/edit')
    return render(request, 'index.html')

def profiles(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.is_superuser:
        return redirect('/')
    if not request.user.profile.phone:
        return redirect('/profile/edit')
    ps = Profile.objects.all().filter(first_name!="")
    profiles = []
    for p in ps:
        email = p.user.email
        temp = {"p":p, "email":email}
        profiles.append(temp)
    return render(request, 'management/index.html', {'profiles': profiles})

def profiles_details(request, request_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.is_superuser:
        return redirect('/')
    if not request.user.profile.phone:
        return redirect('/profile/edit')
    if request.method == 'POST':
        profile = Profile.objects.get(id=request_id)
        permissions_form = PermissionsForm(request.POST, instance=profile)
        if permissions_form.is_valid():
            permissions_form.save()
            return redirect('/management')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile = Profile.objects.get(id=request_id)
        email = profile.user.email
        permissions_form = PermissionsForm(instance=profile)
        return render(request, 'management/detail.html', {'profile': profile, 'email': email, 'permissions_form':permissions_form})


def patient(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.profile.is_doctor:
        return redirect('/')
    if not request.user.profile.phone:
        return redirect('/profile/edit')
    issue_dict = {1:'Blood', 2:'Cancer',3:'Cardiovascular/Heart',4:'Ear',5:'Eye',6:'Infection',7:'Immune',8:'Injury/Accident',
            9:'Mental Health',10:'Metabolic/Endocrine',11:'Muscle/Bone',12:'Neurological',13:'Oral and gastrointestinal',
            14:'Renal and Urogenital',15:'Reproduction/Childbirth',16:'Respiratory',17:'Skin',18:'Stroke',19:'General/Other'}
    sort_form = SortForm()
    if request.method == 'POST':
        patients = Patient.objects.all().filter(doctor__isnull=True, issue=request.POST["issue"]).order_by("-severity")
    else:
        order_by = request.GET.get('order_by')
        if order_by:
            ordering = order_by
        else:
            ordering = 'severity'
        direction = request.GET.get('direction')
        if direction == 'desc':
            ordering = '-{}'.format(ordering)
        patients = Patient.objects.all().filter(doctor__isnull=True).order_by(ordering)
    return render(request, 'patient/index.html', {'patients': patients, 'issue_dict': issue_dict, 'sort_form': sort_form})

def doctor_patients(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.profile.is_doctor:
        return redirect('/')
    if not request.user.profile.phone:
        return redirect('/profile/edit')
    issue_dict = {1:'Blood', 2:'Cancer',3:'Cardiovascular/Heart',4:'Ear',5:'Eye',6:'Infection',7:'Immune',8:'Injury/Accident',
            9:'Mental Health',10:'Metabolic/Endocrine',11:'Muscle/Bone',12:'Neurological',13:'Oral and gastrointestinal',
            14:'Renal and Urogenital',15:'Reproduction/Childbirth',16:'Respiratory',17:'Skin',18:'Stroke',19:'General/Other'}
    sort_form = SortForm()
    if request.method == 'POST':
        patients = Patient.objects.all().filter(doctor=request.user.profile.id, issue=request.POST["issue"]).order_by("-severity")
    else:
        order_by = request.GET.get('order_by')
        if order_by:
            ordering = order_by
        else:
            ordering = 'severity'
        direction = request.GET.get('direction')
        if direction == 'desc':
            ordering = '-{}'.format(ordering)
        patients = Patient.objects.all().filter(doctor=request.user.profile.id).order_by(ordering)
        patient_list = []
        for p in patients:
            regis = p.registrar
            email = regis.user.email
            temp = {"p":p, "r":regis, "email":email}
            patient_list.append(temp)
    return render(request, 'doctor/patients.html', {'patients': patient_list, 'issue_dict': issue_dict, 'sort_form': sort_form})

def doctor_patients_detail(request, request_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.profile.is_doctor:
        return redirect('/')
    if not request.user.profile.phone:
        return redirect('/profile/edit')
    issue_dict = {1:'Blood', 2:'Cancer',3:'Cardiovascular/Heart',4:'Ear',5:'Eye',6:'Infection',7:'Immune',8:'Injury/Accident',
            9:'Mental Health',10:'Metabolic/Endocrine',11:'Muscle/Bone',12:'Neurological',13:'Oral and gastrointestinal',
            14:'Renal and Urogenital',15:'Reproduction/Childbirth',16:'Respiratory',17:'Skin',18:'Stroke',19:'General/Other'}
    order_by = request.GET.get('order_by')
    if order_by:
        ordering = order_by
    else:
        ordering = 'severity'
    direction = request.GET.get('direction')
    if direction == 'desc':
        ordering = '-{}'.format(ordering)
    patient = Patient.objects.get(id=request_id)
    regis = patient.registrar
    email = regis.user.email
    p = {"p":patient, "r":regis, "email": regis.user.email}
    return render(request, 'doctor/detail.html', {'p': p, 'issue_dict': issue_dict})

def detail(request, request_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.profile.phone:
        return redirect('/profile/edit')
    try:
        p = Patient.objects.get(id=request_id)
    except Request.DoesNotExist:
        raise Http404("Patient does not exist")
    if request.method == "POST":
        delVal = request.POST.get('delete')
        grabVal = request.POST.get('grab')
        if grabVal:
            p.doctor=request.user.profile
            p.save()
            return redirect('index')
        elif delVal:
            message = client.messages.create(
                body="A Doctor has accepted your request, expect a text from them soon.",
                from_="+19809490170",
                to=p.phonenumber
            )
            print(message.sid)
            message2 = client.messages.create(
                body="You've approved the patient request, please contact them at %s" %r.phonenumber,
                from_="+19809490170",
                to=str(request.user.profile.phone)
            )
            print(message2.sid)
            p.delete()
            return redirect('index')
        else:
            return redirect('index')
    else:
        return render(request, 'request/detail.html', {'request': p})

def new_patient(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not (request.user.profile.is_doctor or request.user.profile.is_registrar):
        return redirect('/')
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('/patient/new')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        patient_form = PatientForm()
    return render(request, 'patient/new.html', {
        'patient_form': patient_form, 'registrar': request.user.profile.id
    })

def patient_detail(request, patient_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if not request.user.doctor.phone:
        return redirect('/profile/edit')
    try:
        p = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return render(request, 'patient/detail.html', {'request': p})

def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
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
