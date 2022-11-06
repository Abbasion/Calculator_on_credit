from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
from django.template import RequestContext

from calculatorapp.models import Wallet


def home(request):
    return render(request, "home.html")
@login_required()
def calculator(request):

    try:
        c = ''
        # if not request.user.is_authenticated:
        acc = Wallet.objects.get()
        print(acc.balance)

        if acc.balance >=10:
            if request.method =="POST":
                n1 = eval(request.POST.get('num1'))
                n2 = eval(request.POST.get('num2'))
                opr = request.POST.get('opr')

                if opr =="+":
                    c = n1 + n2
                elif opr == "-":
                    c = n1 - n2
                elif opr == "*":
                    c = n1 * n2
                elif opr =="/":
                    c = n1/n2

                acc.balance = acc.balance - 10

                acc.save()
            return render(request, 'Calculator.html', {'c': c, 'wallet': acc})
        else:
            messages.error(request, "you are running out of balance")
            return redirect("calculator")



    except:
        c = "Invalid operator"
    return render(request, 'Calculator.html')


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("calculator")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

    return HttpResponse("login")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def wallet(request):
    try:
        userId = request.user.id
        user = request.user
        print(userId)
        wall = Wallet.objects.get()
        if wall is None:
            if request.method == "POST":
                balance = eval(request.POST['num'])
                # bb = eval(Wallet.balance + balance)
                userId = request.user.id
                wal = Wallet(balance, userId)
                wal.save()
                messages.success(request, "balance has been added to your account")
                return redirect('calculator')
            return render(request, 'wallet.html')
        else:
            if request.method == "POST":
                balance = eval(request.POST.get('num'))
                wall.balance = wall.balance + balance
                wall.save()
                messages.success(request, "balance has been added to your account")
                return redirect('calculator')

            else:
                return render(request, 'wallet.html')
    except:
        pass






# def submitquery(request):
#     q = request.GET['query']
#     try:
#         ans = eval(q)
#         mydictionary = {
#             "q" : q,
#             "ans" : ans,
#             "error" : False,
#             "result" : True
#         }
#         return render(request,'index.html',context=mydictionary)
#     except:
#         mydictionary = {
#             "error" : True,
#             "result" : False
#
#         }
#         return render(request,'index.html',context=mydictionary)