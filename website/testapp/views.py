from django.shortcuts import render
from .models import Employee

from django.http import HttpResponse

def Test2(request):

    return HttpResponse('<body bgcolor="red"> This is Test2 in Testapp <br></body>')

def Empdata(request):
    context={'empdb':Employee.objects.all()}
    return render(request,'employee.html',context)