from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['userfirst_name']) < 2:
            errors['userfirst_name'] = 'First Name should be at least 2 characters'
        if len(post_data['userlast_name']) < 2:
            errors['userlast_name'] = 'Last Name should be at least 2 characters'
        if not EMAIL_REGEX.match(post_data['user_email']):
            errors['email'] = "Invalid email address"
        if len(post_data['user_phone']) != 10:
            errors['user_phone'] = "Phone number must be 10 digits"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"
        try:
            user = User.objects.get(email = post_data['user_email'])
            errors['email_in_use'] = "This email is unavailable"
        except:
            pass
        return errors

class User(models.Model):
    userfirst_name = models.CharField(max_length=60)
    userlast_name = models.CharField(max_length=60)
    user_email = models.CharField(max_length=255)
    user_phone = models.IntegerField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()