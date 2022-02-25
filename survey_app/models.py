from django.db import models
from enroll_app.models import Participant, Caregiver
import re

class DemographicsManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if post_data.get('race') is None:
            errors['race'] = "Race category required"
        if post_data.get('gender') is None:
            errors['gender'] = "Gender category required"
        if post_data.get('grade_level') is None:
            errors['grade_level'] = "Grade level required"
        if post_data.get('household') is None:
            errors['household'] = "Household category required"
        if len(post_data['age']) < 1:
            errors['age'] = "Age required"
        if len(post_data['school']) < 1:
            errors['school'] = "Name of School required"
        return errors


class DemographicsSurvey(models.Model):
    subject = models.ForeignKey(Participant, related_name = "targets", on_delete = models.CASCADE)
    race = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    grade_level = models.CharField(max_length = 5)
    household = models.CharField(max_length = 100)
    age = models.PositiveSmallIntegerField()
    school = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = DemographicsManager()


class InterestManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if post_data.get('referral') is None:
            errors['referral'] = "Referral category required"
        if len(post_data['expectation']) < 1:
            errors['expectation'] = "Expectation field required"
        if len(post_data['goals']) < 1:
            errors['goals'] = "Goals field required"
        if len(post_data['dream_career']) < 1:
            errors['dream_career'] = "Dream career field required"
        if len(post_data['social_issue']) < 1:
            errors['social_issue'] = "Social Issues field required"
        return errors

class InterestSurvey(models.Model):
    interest_subject = models.ForeignKey(Participant, related_name = "interest_survey", on_delete = models.CASCADE)
    referral = models.CharField(max_length = 255)
    expectation = models.TextField()
    goals = models.TextField()
    dream_career = models.TextField()
    social_issue = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = InterestManager()


class CaregiverDemographicsManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if post_data.get('caregiver_race') is None:
            errors['caregiver_race'] = "Race category required"
        if post_data.get('caregiver_gender') is None:
            errors['caregiver_gender'] = "Gender category required"
        if post_data.get('education_level') is None:
            errors['education_level'] = "Education category required"
        if post_data.get('household_income') is None:
            errors['household_income'] = "Income range category required"
        return errors

class CaregiverDemographicsSurvey(models.Model):
    INCOME_LEVEL1 = "1"
    INCOME_LEVEL2 = "2"
    INCOME_LEVEL3 = "3"
    INCOME_LEVEL4 = "4"
    INCOME_LEVEL5 = "5"
    INCOME_LEVEL6 = "6"
    INCOME_LEVEL7 = "7"
    INCOME_LEVEL8 = "8"

    INCOME = (
        (INCOME_LEVEL1, "Less than $10,000"),
        (INCOME_LEVEL2, "$10,000 - $19,000"),
        (INCOME_LEVEL3, "$20,000 - $29,000"),
        (INCOME_LEVEL4, "$30,000 - $39,000"),
        (INCOME_LEVEL5, "$40,000 - $49,000"),
        (INCOME_LEVEL6, "$50,000 - $75,000"),
        (INCOME_LEVEL7, "$75,000 - $100,000"),
        (INCOME_LEVEL8, "$100,000 or More")
    )

    subject_caregiver = models.ForeignKey(Caregiver, related_name = "caregiver_targets", on_delete = models.CASCADE)
    caregiver_race = models.CharField(max_length = 50)
    caregiver_gender = models.CharField(max_length = 50)
    education_level = models.CharField(max_length = 50)
    professional_certs = models.TextField(blank=True)
    household_income = models.CharField(max_length = 60, choices = INCOME)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CaregiverDemographicsManager()


class CaregiverInterestManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['caregiver_expectation']) < 1:
            errors['caregiver_expectation'] = "Expectation field required"
        if len(post_data['caregiver_goals']) < 1:
            errors['caregiver_goals'] = "Goals field required"
        if post_data.get('career') is None:
            errors['career'] = "A Yes or No response required where requested"
        if len(post_data['caregiver_dream_career']) < 1:
            errors['caregiver_dream_career'] = "Dream career field required"
        return errors

class CaregiverInterestSurvey(models.Model):
    caregiver_subject = models.ForeignKey(Caregiver, related_name = "caregiver_interest_survey", on_delete = models.CASCADE)
    caregiver_expectation = models.TextField()
    caregiver_goals = models.TextField()
    caregiver_dream_career = models.TextField()
    career = models.CharField(max_length = 3)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CaregiverInterestManager()


class AssentManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['assentq1']) < 2 or len(post_data['assentq2']) < 2 or len(post_data['assentq3']) < 2 or len(post_data['assentq4']) < 2:
            errors['assentquestions'] = "Short answers should be at least 2 characters"
        if post_data.get('svideo') is None or post_data.get('saudio') is None or post_data.get('sfuture') is None:
            errors['assentoptions'] = "A Yes or No response is required where requested."
        return errors

class IRBAssentSurvey(models.Model):
    irb_assent_subject = models.ForeignKey(Participant, related_name = "assentee", on_delete = models.CASCADE)
    assentq1 = models.CharField(max_length = 255)
    assentq2 = models.CharField(max_length = 255)
    assentq3 = models.CharField(max_length = 255)
    assentq4 = models.CharField(max_length = 255, blank=True)
    svideo = models.CharField(max_length = 3)
    saudio = models.CharField(max_length = 3)
    stusign = models.CharField(max_length = 255)
    sfuture = models.CharField(max_length = 3)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AssentManager()


class ConsentManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['consentq1']) < 2 or len(post_data['consentq2']) < 2 or len(post_data['consentq3']) < 2 or len(post_data['consentq4']) < 2:
            errors['consentquestions'] = "Short answers should be at least 2 characters"
        if post_data.get('cvideo') is None or post_data.get('caudio') is None or post_data.get('cvideohouse') is None or post_data.get('cvideoroom') is None or post_data.get('cvideome') is None or post_data.get('cvideocontents') is None or post_data.get('cfuture') is None:
            errors['consentoptions'] = "A Yes or No response is required where requested."
        return errors
        

class IRBConsentSurvey(models.Model):
    irb_consent_subject = models.ForeignKey(Participant, related_name = "consentee", on_delete = models.CASCADE)
    consentq1 = models.CharField(max_length = 255)
    consentq2 = models.CharField(max_length = 255)
    consentq3 = models.CharField(max_length = 255)
    consentq4 = models.CharField(max_length = 255, blank=True)
    cvideo = models.CharField(max_length = 3)
    caudio = models.CharField(max_length = 3)
    cvideohouse = models.CharField(max_length = 3)
    cvideoroom = models.CharField(max_length = 3)
    cvideome = models.CharField(max_length = 3)
    cvideocontents = models.CharField(max_length = 3)
    csign = models.CharField(max_length = 255)
    cfuture = models.CharField(max_length = 3)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ConsentManager()


class StipendManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        SOC_REGEX = re.compile(r'^[0-9]{3}\-[0-9]{2}\-[0-9]{4}$')
        if post_data.get('talent') is None:
            errors['talent'] = "Yes or No response required for talent release question"
        if post_data.get('payable') is None:
            errors['payable'] = "Payee required"
        if post_data.get('citizen') is None:
            errors['citizen'] = "Yes or No response required for citizenship question"
        if not SOC_REGEX.match(post_data['soc_sec']):
            errors['soc_sec'] = "Social security number has been entered incorrectly. Please follow the example provided."
        if len(post_data['dateofbirth']) != 10:
            errors['dateofbirth'] = "Date of birth has been entered incorrectly. Please follow the example provided."
        return errors

class StipendSurvey(models.Model):
    stipend_subject = models.ForeignKey(Participant, related_name = "stipendapplicant", on_delete = models.CASCADE)
    talent = models.CharField(max_length=3)
    payable = models.CharField(max_length=60)
    citizen = models.CharField(max_length=3)
    soc_sec = models.CharField(max_length=11)
    dateofbirth = models.DateTimeField()
    pmtaddr = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = StipendManager()