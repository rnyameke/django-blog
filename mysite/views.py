from mysite.forms import RegisterForm
from django.views.generic.edit import CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = "register.html"
    success_url = reverse_lazy("login")
    form_class = RegisterForm
    success_message = "Your profile was created successfully"

    def signup(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return reverse_lazy("login") #redirect to login page because auto login isn't working
        else:
            form = UserCreationForm()
        return render(request, "register.html", {"form": form})
