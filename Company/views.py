from django.shortcuts import render, redirect
from .forms import UserLogin
from .models import Agents, Companys
from django.contrib import messages
from cable.models import Bills
from register.models import NewRegister
from transactions.models import Reports, Transaction
import pandas as pd
from datetime import datetime
from django.db.models import Q
import datetime
from datetime import timedelta
from apfiber.mypublic import callmenu
import janitor
import razorpay
import json


today = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()

client = razorpay.Client(auth=(""))


def login(request):
    if 'userId' in request.session:
        Context = dict()
        Context['welcome'] = request.session['name']
        return render(request, 'dashboard.html', Context)
    else:
        companys = Companys.objects.using("default").all()
        myform = UserLogin()
        Context = dict()
        Context['myform'] = myform
        Context['companys'] = companys
        return render(request, 'login.html', Context)


def payment(request):
    try:
        return render(request,'index.html')
    except:
        return render(request, 'index.html')

def payamount(request):
    try:
        if request.method == 'POST':


            camount = request.POST['amount']
            payamt = request.POST['amount']
            cname = request.POST['cname']
            cnumber = request.POST['cnumber']
            cid = request.POST['cid']
            ctotal = request.POST['ctotal']
            print(cname)
            print(cnumber)
            print(cid)
            cus_paid = camount
            camount = int(camount)
            camount = (camount*100)+camount
            print(camount)
            request.session['cus_amount'] = camount
            request.session['caf_number'] = caf_number
            request.session['cus_paid'] = cus_paid
            request.session['payamt'] = payamt
            request.session['cname'] = cname
            request.session['cnumber'] = cnumber
            request.session['cid'] = cid
            request.session['ctotal'] = ctotal
            Context = dict()
            Context['camount'] = camount
            Context['cname'] = cname
            Context['cnumber'] = cnumber
    
            return render(request,'payment3.html',Context)

    except:
        return render(request, 'index.html')       

def charge(request):
    try:
        if request.method == 'POST':
            payment_id = request.POST['razorpay_payment_id']
            payment_amount = request.session['cus_amount']
            print(payment_amount)
            payment_currency = "INR"
            resp = client.payment.capture(payment_id, payment_amount, {"currency": payment_currency})
            print(resp)
            pay_id = resp['id']
            pay_amount = resp['amount']
            pay_method = resp['method']
            pay_refund = resp['amount_refunded']
            pay_bank = resp['bank']
            pay_fee = resp['fee']
            pay_tax = resp['tax']
            pay_amount = int(pay_amount)
    
            ctotal = request.session['ctotal']
            payamt = request.session['payamt']
            cid = request.session['cid']
            caf_number = request.session['caf_number']
            cus_number = request.session['cnumber']
            cus_name = request.session['cname']
            # plan = request.session['plan']
            ctotal = int(float(ctotal))
            print(ctotal)
            payamt = int(payamt)
            pay_act_tot = (ctotal + payamt)
            print(pay_act_tot)
            cus_paid_amount= request.session['cus_paid']


            cid = int(cid)
            print(cid)



            Bills.objects.filter(id=cid).update(Lien_men="Razorpay",paid=cus_paid_amount,Time=current_time ,total_balance = pay_act_tot,flag =1)


            obj = Transaction(agent_id=99, agent_name="Razorpay", CAF_Number=caf_number,txn_id=pay_id,customer_mobile=cus_number, customer_name=cus_name, transaction_type=pay_method,paid_amount=cus_paid_amount,balance_amount=pay_act_tot,Date=today, Time = current_time)
            obj.save()



            request.session.flush()
            return render(request,'success.html')
    except:
        return render(request, 'index.html')


def pay(request):
    try:
        if request.method ==  'POST':
            data = request.POST['data']
            flag = 0
            print(data)
            print(today)

            caf_data = Bills.objects.filter(Q(CAF_Number = data) | Q(Box_number = data) | Q(Customer_Mobile = data) , Q(flag = flag)).values()
            if caf_data:
                Context = dict()
                Context['data'] = data
                print (caf_data)
                Context['caf_data'] = caf_data
                return render(request,'payment2.html', Context)
            else:
                messages.error(request, 'Sorry! Wrong CAF NUMBER OR PAYMENT FOR THIS CAF IS ALREADY DONE', 'alert-danger')
                return redirect('/payment/')
        messages.error(request, 'Sorry! Wrong CAF NUMBER OR PAYMENT FOR THIS CAF IS ALREADY DONE', 'alert-danger')

        return redirect('/payment/')

    except:
        messages.error(request, 'Sorry! Wrong CAF NUMBER OR PAYMENT FOR THIS CAF IS ALREADY DONE', 'alert-danger')
        return redirect('/payment/')


def checkuser(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            if username == 'tln':
                results = Companys.objects.filter(password=password).values()

            else:
                results = Companys.objects.filter(username=username, password=password).values()
                print(results)
                print("tlnnlllasfdalfs")

            if results:
                for row in results:
                    if username == 'tln':
                        request.session['userId'] = row['id']
                        request.session['name'] = username
                        request.session['username'] = username
                        request.session['password'] = row['password']
                        request.session['mobile'] = row['mobile']



                    else:
                        request.session['userId'] = row['id']
                        request.session['name'] = username
                        request.session['username'] = username
                        request.session['password'] = row['password']
                        request.session['mobile'] = row['mobile']

                return redirect('/dashboard/')
            else:
                messages.error(request, 'Sorry! Wrong Username or Wrong Password', 'alert-danger')
                return redirect('/')


    except:
        messages.error(request, 'Sorry! Wrong Username or Wrong Password', 'alert-danger')
        return redirect('/')


def dashboard(request):
    df = pd.DataFrame(list(Bills.objects.all().values()))
    df4 = pd.DataFrame(list(Transaction.objects.all().values()))
    df5 = df4['id']
    txn_type = df4['transaction_type']
    txn_date = df4['Date']
    txn_phonepe = txn_type.loc[txn_type == "PhonePe"]
    txn_gpay = txn_type.loc[txn_type == "GooglePay"]
    txn_cash = txn_type.loc[txn_type == "Cash"]
    j = []
    for i in txn_date:
        if (i == today):
            j.append(i)
    df_filtered = df4.filter_date('Date', today, today)
    df_filtered_txn_type = df_filtered['transaction_type']
    today_phonepe = df_filtered_txn_type.loc[df_filtered_txn_type == "PhonePe"]
    today_phonepe = today_phonepe.count()
    today_googlepay = df_filtered_txn_type.loc[df_filtered_txn_type == "GooglePay"]
    today_googlepay = today_googlepay.count()
    today_cash = df_filtered_txn_type.loc[df_filtered_txn_type == "Cash"]
    today_cash = today_cash.count()

    today_txn = len(j)
    txn_phonepe = txn_phonepe.count()
    txn_gpay = txn_gpay.count()
    txn_cash = txn_cash.count()
    txn_data = df5.count()

    df3 = pd.DataFrame(list(Agents.objects.all().values()))
    data = df['id']
    df2 = df['Status']
    data = data.count()

    agent_data = df3['name']
    adata = agent_data.count()
    s = df2.loc[df2 == "Active"]
    active = s.count()
    inactive = data - active
    cnt = df['id']
    cnt = cnt.count()
    print(cnt)
    agents = adata

    graph = []

    gdata = {
        "Cable Bills": cnt,
        "Active Users": active,
        "Inactive Users": inactive,
        "Agents": agents,

    }
    graph.append(gdata)

    Context = dict()
    Context['cbills'] = cnt
    Context['active'] = active
    Context['agents'] = agents
    Context['inactive'] = inactive
    Context['graph'] = graph
    Context['total_txn'] = txn_data
    Context['txn_phone'] = txn_phonepe
    Context['txn_gpay'] = txn_gpay
    Context['txn_cash'] = txn_cash
    Context['today_txn'] = today_txn
    Context['today_phonepe'] = today_phonepe
    Context['today_googlepay'] = today_googlepay
    Context['today_cash'] = today_cash

    return render(request, 'dashboard.html', Context)


def logout(request):
    request.session.flush()
    return redirect('/')


def companaydit(request):
    company = Companys.objects.get(id=1)
    return company
