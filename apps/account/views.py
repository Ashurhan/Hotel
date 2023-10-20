from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm  , LoginForm , UserBaseForm
from .models import User

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
        else:
            return render(request, "sign-up.html", {"form": form})
    else:   
        return render(request, "sign-up.html", {"form": form})
    

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        user = authenticate(username=form.data["username"], password=form.data["password"])
        if user is not None:
            login(request, user)
            return redirect("page")
        else:
            return render(request, "sign-in.html", {"form": form, "error": "Неверное имя пользователя или пароль!"})
    else:
        return render(request, "sign-in.html", {"form": form})
    


def logout_view(request):
    logout(request)
    return redirect("login")



from django.shortcuts import render, redirect

def update_profile_view(request):
    user = request.user

    if request.method == "GET":
        base_form = UserBaseForm(instance=user)
        return render(request, "edit_profile.html", {"user": user, "base_form": base_form})

    if request.method == "POST":
        base_form = UserBaseForm(data=request.POST, instance=request.user, files=request.FILES)

        if base_form.is_valid():
            base_form.save()
            return redirect("profile")
        else:
            return render(request, "edit_profile.html", {"user": user, "base_form": base_form})

    # Return a default response for other cases (e.g., unsupported request method)
    return render(request, "edit_profile.html", {"user": user, "base_form": base_form})

    