from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Participant, Caregiver, OtherContact
from loginreg_app.models import User

def index(request):
    if 'user_id' in request.session:
        return redirect("/login/logout")
    return render(request, "Home.html")

def dashboard(request):
    context = {
        "participants": Participant.objects.all(),
        "admin": User.objects.first()
    }
    if not 'user_id' in request.session:
        messages.error(request, "Please log in to access this page")
        return redirect("/login/signin")
    return render(request, "dashboard.html", context)

def add_participant(request):
    context = {
        "participants": Participant.objects.all()
    }
    return render(request, "add_participant.html", context)

def create_participant(request):
    errors = Participant.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/participant/add_participant")
    else:
        participant = Participant.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            address = request.POST['address'],
            city = request.POST['city'],
            state = request.POST['state'],
            zip_code = request.POST['zip_code']
        )
    return redirect(f"/participant/{participant.id}/add_caregiver")

def delete_participant(request, participant_id):
    participant = Participant.objects.get(id = participant_id)
    if participant.caregivers.exists():
        for caregiver in participant.caregivers.all():
            caregiver.delete()
    participant.delete()
    return redirect("/dashboard")

def edit_participant(request, participant_id):
    context = {
        "participant": Participant.objects.get(id = participant_id),
    }
    return render(request, "edit_participant.html", context)

def update_participant(request, participant_id):
    participant = Participant.objects.get(id = participant_id)
    participant.first_name = request.POST['first_name']
    participant.last_name = request.POST['last_name']
    participant.email = request.POST['email']
    participant.phone = request.POST['phone']
    participant.address = request.POST['address']
    participant.city = request.POST['city']
    participant.state = request.POST['state']
    participant.zip_code = request.POST['zip_code']
    participant.enrollment = request.POST['enrollment']
    participant.participation = request.POST['participation']
    if request.POST['enroll_date']== "":
        participant.enroll_date = None
    else:
        participant.enroll_date = request.POST['enroll_date']
    participant.save()
    return redirect("/dashboard")

def add_caregiver(request, participant_id):
    context = {
        "participant": Participant.objects.get(id=participant_id)
    }
    return render(request, "add_caregiver.html", context)

def create_caregiver(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    errors = Caregiver.objects.basic_validator(request.POST)
    if errors:
        if participant.caregivers.exists():
            for key, value in errors.items():
                messages.error(request, value)
                return redirect(f"/participant/{participant_id}/more_caregivers")
        else:
            for k, v in errors.items():
                messages.error(request, v)
                return redirect(f"/participant/{participant_id}/add_caregiver")
    else:
        if not Caregiver.objects.filter(email = request.POST['email']).exists():
            this_caregiver = Caregiver.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                phone = request.POST['phone'],
                relationship = request.POST['relationship']
            )        
            participant.caregivers.add(this_caregiver)
        else:
            existing_caregiver = Caregiver.objects.filter(email = request.POST['email'])
            for add_match in existing_caregiver:
                participant.caregivers.add(add_match)
        if participant.caregivers.count() < 2:
            return redirect (f"/participant/{participant_id}/more_caregivers")
        else:
            return redirect(f"/survey/{participant_id}/add_demographics")

def profile_page(request, participant_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
    }
    return render(request, "profile.html", context)

def add_more_caregivers(request, participant_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
    }
    return render(request, "caregiver2.html", context)

def create_contact(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    errors = OtherContact.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/participant/{participant_id}/more_caregivers")
    else:
        OtherContact.objects.create(
            student = participant,
            name = request.POST['contact_name'],
            email = request.POST['contact_email'],
            phone = request.POST['contact_phone']
        )
        return redirect(f"/survey/{participant_id}/add_demographics")

def remove_caregiver(request, participant_id, caregiver_id):
    participant = Participant.objects.get(id=participant_id)
    this_caregiver = Caregiver.objects.get(id=caregiver_id)
    participant.caregivers.remove(this_caregiver)
    return redirect("/participant/{participant_id}/profile")

def edit_caregiver(request, participant_id, caregiver_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
        "this_caregiver": Caregiver.objects.get(id=caregiver_id)
    }
    return render(request, "edit_caregiver.html", context)
    
def update_caregiver(request, participant_id, caregiver_id):
    participant = Participant.objects.get(id=participant_id)
    this_caregiver = participant.caregivers.get(id=caregiver_id)
    this_caregiver.name = request.POST['name']
    this_caregiver.email = request.POST['email']
    this_caregiver.phone = request.POST['phone']
    this_caregiver.save()
    return redirect(f"/participant/{participant_id}/profile")

def delete_caregiver(request, participant_id, caregiver_id):
    participant = Participant.objects.get(id=participant_id)
    this_caregiver = participant.caregivers.get(id=caregiver_id)
    this_caregiver.delete()
    return redirect(f"/participant/{participant_id}/profile")

def edit_contact(request, participant_id, contact_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
        "this_contact": OtherContact.objects.get(id=contact_id)
    }
    return render(request, "edit_contact.html", context)


def update_contact(request, participant_id, contact_id):
    participant = Participant.objects.get(id=participant_id)
    this_contact = participant.contact.get(id=contact_id)
    this_contact.name = request.POST['contact_name']
    this_contact.email = request.POST['contact_email']
    this_contact.phone = request.POST['contact_phone']
    this_contact.save()
    return redirect(f"/participant/{participant_id}/profile")

def delete_contact(request, participant_id, contact_id):
    participant = Participant.objects.get(id=participant_id)
    this_contact = participant.contact.get(id=contact_id)
    this_contact.delete()
    return redirect(f"/participant/{participant_id}/profile")

def progress_page(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    c1 = participant.caregivers.first()
    count = 0
    half = False
    onethird = False
    twothirds = False
    complete = False
    for cgs in participant.caregivers.all():
        if participant.caregivers.count() > 1:
            count += cgs.caregiver_interest_survey.count()
            if participant.stipendapplicant.exists():
                twothirds = True
            else:
                onethird = True
        else:
            half = True
            if participant.stipendapplicant.exists():
                complete = True
        if twothirds and count > 1:
            complete = True
    context = {
        "participant": Participant.objects.get(id=participant_id),
        "caregivers": participant.caregivers.all(),
        "c1": c1,
        "onethird": onethird,
        "half": half,
        "twothirds": twothirds,
        "complete": complete
    }
    return render(request, "progress_page.html", context)

def success_page(request, participant_id):
    return render(request, "success_page.html")

def contact_us(request):
    return render(request, "contactus.html")

def about(request):
    return render(request, "about.html")

def responses(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    context = {
        "participant": participant,
        "assentresponses": participant.assentee.all(),
        "consentresponses": participant.consentee.all(),
        "stipendresponses": participant.stipendapplicant.all()
    }
    return render(request, "responses.html", context)