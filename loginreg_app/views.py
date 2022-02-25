from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User
import bcrypt

def login_page(request):
    return render(request, "signin_page.html")

def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/login/register")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            userfirst_name = request.POST['userfirst_name'],
            userlast_name = request.POST['userlast_name'],
            user_email = request.POST['user_email'],
            user_phone = request.POST['user_phone'],
            password = pw_hash
        )
        messages.info(request, "Please log in")
    return redirect ("/login/signin")

def registration_page(request):
    return render(request, "registration_page.html")

def login_user(request):
    try:
        user = User.objects.get(user_email = request.POST['user_email'])
    except:
        messages.error(request, "Email address or password is incorrect")
        return redirect("/login/signin")
    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Email address or password is incorrect")
        return redirect("/login/signin")
    else:
        request.session['user_id'] = user.id
        request.session['user_email'] = user.user_email
        request.session['userfirst_name'] = user.userfirst_name
        request.session['userlast_name'] = user.userlast_name
    return redirect ("/dashboard")
    

def logout_user(request):
    request.session.clear()
    return redirect("/")

def teamroster(request):
    context = {
        "team": User.objects.all(),
        "admin": User.objects.first()
    }
    return render(request, "team.html", context)

def edit_user(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, "edit_user.html", context)

def update_user(request, user_id):
    user = User.objects.get(id = user_id)
    user.userfirst_name = request.POST['first_name']
    user.userlast_name = request.POST['last_name']
    user.user_email = request.POST['email']
    user.user_phone = request.POST['phone']
    user.save()
    return redirect("/login/teamroster")

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect("/login/teamroster")