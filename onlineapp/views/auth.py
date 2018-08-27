from onlineapp.models import College
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import *
from django.shortcuts import *
from onlineapp.forms import *
#from django.contrib.messages import constants as messages
from django.contrib import messages

def logout_user(request):
    logout(request)
    return redirect('login')


class SignUpView(View):
    def get(self,request, *args, **kwargs):
        sign_up_form = SignUpForm()
        context = {
            'title' : 'sign-up page',
            'form' : sign_up_form,
            'error' : kwargs.get('error')
        }
        return render(
            request,
            'sign_up.html',
            context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            user = authenticate(
                request,
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
            if(user is not None):
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid Credentials")
                return render(request, 'sign_up.html', {'error': True})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        login_form = LoginForm()
        context = {
            'title' : 'Login page',
            'form' : login_form
        }
        return render(request, "login.html", context)
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            user = authenticate(**form.cleaned_data)
            if(user):
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Error in loggnig in")
                return redirect('login',**{'error' : True})