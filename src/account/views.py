from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):

    context = {}
    return render(request, 'homepage.html', context)


def login(request):
    pass



def logout(request):
    pass

