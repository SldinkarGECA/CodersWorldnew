from django.shortcuts import render

# from django.contrib.auth.models import User
from .models import Person

# importing the Homepage model
from django.apps import apps

Homepage = apps.get_model(app_label="homepage",
                          model_name="Homepage")

# mail
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["psw"]
        user = Person.objects.get(username=username)
        if user is not None and user.password == password:
            categories = Homepage.objects.all()
            request.session["name"] = user.name
            return render(
                request,
                "homepage/homepage.html",
                {"categories": categories,
                 "name": request.session["name"]},
            )

        else:
            return render(
                request,
                "accounts/login.html",
                {
                    "username": "Username and Password doesnot match"},
            )
    else:
        return render(request, "accounts/login.html")


def logout(request):
    request.session["name"] = None
    categories = Homepage.objects.all()
    return render(request, "homepage/homepage.html",
                  {"categories": categories})


def register(request):
    if request.method == "POST":
        if request.POST["psw"] == request.POST[
            "psw-repeat"]:
            try:
                user = Person.objects.get(
                    username=request.POST["username"])
                return render(
                    request,
                    "accounts/register.html",
                    {
                        "username": "This username already exists!!"},
                )
            except:
                user = Person(
                    name=request.POST["name"],
                    username=request.POST["username"],
                    password=request.POST["psw"],
                    email=request.POST["email"],
                )

                # sending mail
                try:
                    user_email = request.POST["email"]
                    subject = "Thank you for registering to CodersWorld!!"
                    message = (
                            "Your username is "
                            + request.POST["username"]
                            + " and password is "
                            + request.POST["psw"]
                            + ".\n Use this details to login!!"
                    )
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user_email]
                    send_mail(subject, message, email_from,
                              recipient_list)
                    user.save()
                except:
                    return render(
                        request,
                        "accounts/register.html",
                        {
                            "error": "Something error occured!! Check your email"},
                    )
                return render(
                    request,
                    "accounts/register.html",
                    {
                        "success": "Registration Suceessful!!"},
                )
        else:
            return render(
                request, "accounts/register.html",
                {"error": "Passwords doesnot match"},
            )
    else:
        return render(request, "accounts/register.html")
