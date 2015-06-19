from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms1 import LoginForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})





def logout(request):
    pass

