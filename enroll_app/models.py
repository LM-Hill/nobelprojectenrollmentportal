from django.db import models
from loginreg_app.models import User
import re

class ParticipantManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PHONE_REGEX = re.compile(r'^[0-9]{10}$')
        if len (post_data['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters"
        if len (post_data['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address"
        if not PHONE_REGEX.match(post_data['phone']):
            errors['phone'] = "Phone number must be 10 digits"
        if len (post_data['address']) < 1:
            errors['address'] = "Address required."
        if len (post_data['city']) < 1:
            errors['city'] = "City required."
        if len (post_data['state']) != 2:
            errors['state'] = "State must be two(2) characters."
        if len (post_data['zip_code']) != 5:
            errors['zip_code'] = "Zip code must be 5 digiits"
        return errors

class Participant(models.Model):
    NOT_ENROLLED = "not_enrolled"
    PENDING = "pending"
    ENROLLED = "enrolled"

    ENROLLMENT_STATUS = (
        (NOT_ENROLLED, "Not Enrolled"),
        (PENDING, "Enrollment Pending"),
        (ENROLLED, "Enrolled")
    )

    INACTIVE = "inactive"
    ACTIVE = "active"

    PARTICIPATION_STATUS = (
        (INACTIVE, "Inactive"),
        (ACTIVE, "Active")
    )

    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 255)
    phone = models.IntegerField()
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)
    enrollment = models.CharField(max_length = 20, choices = ENROLLMENT_STATUS, default = NOT_ENROLLED)
    participation = models.CharField(max_length = 8, choices = PARTICIPATION_STATUS, default = INACTIVE)
    enroll_date = models.DateTimeField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ParticipantManager()


class CaregiverManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PHONE_REGEX = re.compile(r'^[0-9]{10}$')
        if len (post_data['name']) < 2:
            errors['name'] = "Name should be at least 2 characters"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address"
        if not PHONE_REGEX.match(post_data['phone']):
            errors['phone'] = "Phone number must be 10 digits"
        if len (post_data['relationship']) < 1:
            errors['relationship'] = "Relationship required."
        return errors

class Caregiver(models.Model):
    name = models.CharField(max_length = 255)
    kids = models.ManyToManyField(Participant, related_name="caregivers")
    email = models.CharField(max_length = 255)
    phone = models.IntegerField()
    relationship = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CaregiverManager()


class ContactManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PHONE_REGEX = re.compile(r'^[0-9]{10}$')
        if len (post_data['contact_name']) < 2:
            errors['contact_name'] = "Name should be at least 2 characters"
        if not EMAIL_REGEX.match(post_data['contact_email']):
            errors['contact_email'] = "Invalid email address"
        if not PHONE_REGEX.match(post_data['contact_phone']):
            errors['contact_phone'] = "Phone number must be 10 digits"
        return errors

class OtherContact(models.Model):
    student = models.ForeignKey(Participant, related_name = "contact", on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ContactManager()