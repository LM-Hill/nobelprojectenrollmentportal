from django.shortcuts import render, redirect
from django.contrib import messages
from . models import DemographicsSurvey, InterestSurvey, CaregiverDemographicsSurvey, CaregiverInterestSurvey, IRBAssentSurvey,IRBConsentSurvey, StipendSurvey
from enroll_app.models import Participant, Caregiver

def survey_page(request, participant_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
        "demographics": DemographicsSurvey.objects.get(subject_id=participant_id)
    }
    return render (request, "survey_page.html", context)

def demographics_survey(request, participant_id):
    context = {
        "participant": Participant.objects.get(id=participant_id)
    }
    return render (request, "demographics.html", context)

def create_demographics(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    errors = DemographicsSurvey.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/survey/{participant_id}/add_demographics")
    else:
        DemographicsSurvey.objects.create(
            subject = participant,
            race = request.POST.get('race'),
            gender = request.POST.get('gender'),
            grade_level = request.POST.get('grade_level'),
            household = request.POST.get('household'),
            age = request.POST['age'],
            school = request.POST['school']
        )
        empty_demo_race = DemographicsSurvey.objects.filter(race = "")
        for p_race in empty_demo_race:
            this_p_race = empty_demo_race.get(id=p_race.id)
            this_p_race.race = request.POST['other_race']
            this_p_race.save()
        empty_demo_gender = DemographicsSurvey.objects.filter(gender = "")
        for p_gender in empty_demo_gender:
            this_p_gender = empty_demo_gender.get(id=p_gender.id)
            this_p_gender.gender = request.POST['other_gender']
            this_p_gender.save()
        empty_demo_household = DemographicsSurvey.objects.filter(household = "")
        for p_household in empty_demo_household:
            this_p_household = empty_demo_household.get(id=p_household.id)
            this_p_household.household = request.POST['other_household']
            this_p_household.save()
        return redirect(f"/survey/{participant_id}/add_interest_survey")

def caregiver_demographics_survey(request, participant_id, caregiver_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
        "caregiver": Caregiver.objects.get(id=caregiver_id)
    }
    return render (request, "caregiver_demographics.html", context)

def create_caregiver_demographics(request, participant_id, caregiver_id):
    participant = Participant.objects.get(id=participant_id)
    caregiver = Caregiver.objects.get(id=caregiver_id)
    errors = CaregiverDemographicsSurvey.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/survey/{participant_id}/{caregiver_id}/add_caregiver_demographics")
    else:
        CaregiverDemographicsSurvey.objects.create(
            subject_caregiver = caregiver,
            caregiver_race = request.POST.get('caregiver_race'),
            caregiver_gender = request.POST.get('caregiver_gender'),
            education_level = request.POST.get('education_level'),
            professional_certs = request.POST['professional_certs'],
            household_income = request.POST.get('household_income')
        )
        empty_demo_c_race = CaregiverDemographicsSurvey.objects.filter(caregiver_race = "")
        for c_race in empty_demo_c_race:
            this_c_race = empty_demo_c_race.get(id=c_race.id)
            this_c_race.caregiver_race = request.POST['other_caregiver_race']
            this_c_race.save()
        empty_demo_c_gender = CaregiverDemographicsSurvey.objects.filter(caregiver_gender = "")
        for c_gender in empty_demo_c_gender:
            this_c_gender = empty_demo_c_gender.get(id=c_gender.id)
            this_c_gender.caregiver_gender = request.POST['other_caregiver_gender']
            this_c_gender.save()
        return redirect(f"/survey/{participant_id}/{caregiver_id}/add_caregiver_interest")

def caregiver_survey_page(request, participant_id, caregiver_id):
    caregiver_demographics = CaregiverDemographicsSurvey.objects.get(subject_caregiver_id=caregiver_id)
    context = {
        "participant":Participant.objects.get(id=participant_id),
        "caregiver": Caregiver.objects.get(id=caregiver_id),
        "caregiver_demographics": CaregiverDemographicsSurvey.objects.get(subject_caregiver_id=caregiver_id)
    }
    return render(request, "caregiver_survey_page.html", context)

def interest_survey(request, participant_id):
    context = {
        "participant": Participant.objects.get(id=participant_id)
    }
    return render(request, "interest_survey.html", context)

def create_interest_survey(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    errors = InterestSurvey.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/survey/{participant_id}/add_interest_survey")
    else:
        InterestSurvey.objects.create(
            interest_subject = participant,
            referral = request.POST.get('referral'),
            expectation = request.POST['expectation'],
            goals = request.POST['goals'],
            dream_career = request.POST['dream_career'],
            social_issue = request.POST['social_issue']
        )
        return redirect(f"/survey/{participant_id}/add_assent_form")

def add_caregiver_interest(request, participant_id, caregiver_id):
    context = {
        "caregiver": Caregiver.objects.get(id=caregiver_id),
        "participant": Participant.objects.get(id=participant_id)
    }
    return render(request, "caregiver_interest_survey.html", context)

def create_caregiver_interest(request, participant_id, caregiver_id):
    first_care = False
    participant = Participant.objects.get(id=participant_id)
    caregiver = Caregiver.objects.get(id=caregiver_id)
    c1=participant.caregivers.first()
    if caregiver.id == c1.id:
        first_care = True
    errors = CaregiverInterestSurvey.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/survey/{participant_id}/{caregiver_id}/add_caregiver_interest")
    else:
        CaregiverInterestSurvey.objects.create(
            caregiver_subject = caregiver,
            caregiver_expectation = request.POST['caregiver_expectation'],
            caregiver_dream_career = request.POST['caregiver_dream_career'],
            career = request.POST.get('career'),
            caregiver_goals = request.POST['caregiver_goals'],                 
        )
        if first_care:
            return redirect(f"/survey/{participant_id}/{caregiver_id}/add_consent_form")
        else:
            return redirect(f"/{participant_id}/progress")

def add_assent_form(request, participant_id):
    context = {
        "participant": Participant.objects.get(id=participant_id)
    }
    return render(request, "assent_form.html", context)

def create_assent_form(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    errors = IRBAssentSurvey.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/survey/{participant_id}/add_assent_form")
    else:
        IRBAssentSurvey.objects.create(
            irb_assent_subject = participant,
            assentq1 = request.POST['assentq1'],
            assentq2 = request.POST['assentq2'],
            assentq3 = request.POST['assentq3'],
            assentq4 = request.POST['assentq4'],
            svideo = request.POST.get('svideo'),
            saudio = request.POST.get('saudio'),
            stusign = request.POST['stusign'],
            sfuture = request.POST.get('sfuture')        
        )
        return redirect(f"/{participant_id}/progress")

def add_consent_form(request, participant_id, caregiver_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
        "caregiver": Caregiver.objects.get(id=caregiver_id)
    }
    return render(request, "consent_form.html", context)
    

def create_consent_form(request, participant_id, caregiver_id):
    participant = Participant.objects.get(id=participant_id)
    caregiver = Caregiver.objects.get(id=caregiver_id)
    errors = IRBConsentSurvey.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/survey/{participant_id}/{caregiver_id}/add_consent_form")
    else:
        IRBConsentSurvey.objects.create(
            irb_consent_subject = participant,
            consentq1 = request.POST['consentq1'],
            consentq2 = request.POST['consentq2'],
            consentq3 = request.POST['consentq3'],
            consentq4 = request.POST['consentq4'],
            cvideo = request.POST.get('cvideo'),
            caudio = request.POST.get('caudio'),
            cvideohouse = request.POST.get('cvideohouse'),
            cvideoroom = request.POST.get('cvideoroom'),
            cvideome = request.POST.get('cvideome'),
            cvideocontents = request.POST.get('cvideocontents'),
            csign = request.POST['csign'],
            cfuture = request.POST.get('cfuture')
        )
        return redirect(f"/survey/{participant_id}/{caregiver_id}/add_stipend_form")

def add_stipend_form(request, participant_id, caregiver_id):
    context = {
        "participant": Participant.objects.get(id=participant_id),
        "caregiver": Caregiver.objects.get(id=caregiver_id)
    }
    return render(request, "stipend_form.html", context)

def create_stipend_form(request, participant_id, caregiver_id):
    participant = Participant.objects.get(id=participant_id)
    caregiver = Caregiver.objects.get(id=caregiver_id)
    errors = StipendSurvey.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/survey/{participant_id}/{caregiver_id}/add_stipend_form")
    else:
        StipendSurvey.objects.create(
            stipend_subject = participant,
            talent = request.POST.get('talent'),
            payable = request.POST.get('payable'),
            citizen = request.POST.get('citizen'),
            soc_sec = request.POST['soc_sec'],
            dateofbirth = request.POST['dateofbirth'],
            pmtaddr = request.POST['pmtaddr']
        )
        return redirect(f"/{participant_id}/progress")