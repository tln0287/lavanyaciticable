from django.shortcuts import render,redirect
from Company.models import Agents,Companys
from django.contrib import messages
from .models import Bills
from register.models import NewRegister
import pandas as pd

# Create your views here.

def reports(request):
    if 'userId' not in request.session:
        return redirect('/')
    else:
        Context = dict()
        Context['welcome'] = request.session['name']
        Context['userpic'] = request.session['image']

        return render(request,'reports.html',Context)
