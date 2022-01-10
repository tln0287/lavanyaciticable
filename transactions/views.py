from django.shortcuts import render,redirect
from Company.models import Agents,Companys
from django.contrib import messages
from cable.models import Bills
from .models import Transaction, Reports
from register.models import NewRegister
import pandas as pd
# Create your views here.



def treport(request):
    if 'userId' not in request.session:
        return redirect('/')
    else:
        df3 = pd.DataFrame(list(Transaction.objects.all().values()))
        tdata = df3['id']
        txn_data = tdata.count()
        #
        # graph = []
        #
        # s = df2.loc[df2 == "Active"]
        # active = s.count()
        # inactive = data - active
        # cnt = df['id']
        # cnt = cnt.count()
        # print(cnt)
        # agents = 25
        # gdata = {
        #     "Cable Bills": cnt,
        #     "Active Users": active,
        #     "Inactive Users": inactive,
        #     "Agents": agents,
        #
        # }
        # graph.append(gdata)
    
        # Context['cbills'] = cnt
        # Context['active'] = active
        # Context['agents'] = agents
        # Context['inactive'] = inactive
        # Context['graph'] = graph
        Context = dict()
        Context['welcome'] = request.session['name']
        Context['userpic'] = request.session['image']

        return render(request,'treport.html',Context)

def agent_report(request):
    if 'userId' not in request.session:
        return redirect('/')
    else:
        Context = dict()
        Context['welcome'] = request.session['name']
        Context['userpic'] = request.session['image']

        return render(request,'agent_report.html',Context)