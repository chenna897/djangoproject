from django.shortcuts import render
from django.http import HttpResponse  

def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

def index(request):  
    return render(request,'index.html')   

def setsession(request):  
    request.session['sname'] = 'chenna'  
    request.session['semail'] = 'chenna.kesava@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);  

