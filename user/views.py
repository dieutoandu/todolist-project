from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def user_login(request):
    massage = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            massage = "user or password erro"
        else:
            login(request, user)
            massage = "login pass "
            return redirect("todolist")

    return render(request, "user/login.html", {"massage": massage})


# Create your views here.
def user_register(request):
    massage = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("POST !", request.POST)

        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, password1, password2)

        if password1 != password2:
            massage = "two password is not pass !"
        elif len(password1) < 8:
            massage = "your password is not 8 "
        else:
            user = User.objects.filter(username=username)
            if user:
                massage = "this user is in"
            else:
                User.objects.create_user(username=username, password=password1)
                User.save()
                massage = "all_pass ! "
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form, "massage": massage})
