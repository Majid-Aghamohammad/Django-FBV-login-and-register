from django.shortcuts import render
from django.template.loader import get_template
from . import forms
from .forms import singup_form,login_form
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
################################################################################
#show home_page
def home_page(request):
    return render(request,'../templates/home.html')
################################################################################
#registration:
def singup_page(request):
    registred=False
    if request.method == "POST":
        sing_up_form =singup_form(request.POST)
        #Inforamation validation
        if sing_up_form.is_valid():
            print(sing_up_form.is_valid())
            user=sing_up_form.save()
            user.set_password(user.password)
            user.save()
            registred=True
            return HttpResponseRedirect(reverse('registred'))
        else:
            print(sing_up_form.errors)
            #IF registration not to be valid show the form agin
    else:
        sing_up_form=singup_form()

    return render(request,'../templates/registration/registration.html',{'singup_form':sing_up_form})
################################################################################
#login
def user_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        print(user)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/sucsse/')

            else:
                #show login agin
                return HttpResponseRedirect(reverse('user_login'))
        else:
            print("someone login failed")
            return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request,'../templates/registration/login.html')
################################################################################
#after_login
def sucsse_page(request):
    return render(request,'../templates/registration/sucsse.html')
################################################################################
#registred
def registred_page(request):
    form=forms.login_form()
    return render(request,'../templates/registration/registred.html')
################################################################################
#log out
@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
################################################################################
