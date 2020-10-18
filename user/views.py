from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse

from user.forms import CustomUserCreationForm
from django.views.generic.edit import FormView

# Create your views here.
class RegisterUserView(FormView):
    template_name = "registration/signup.html"    
    form_class = CustomUserCreationForm

    def post(request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
