from django.shortcuts import render

from app.models import *

# Create your views here.

def Data_Dept(request):
    lot=Dept.objects.all()
    d={'data':lot}
    return render(request,'Datas_dept.html',d)

def Data_Emp(request):
    lo=Emp.objects.all()
    d={'Ram':lo}
    return render(request,'Datas_emp.html',d)