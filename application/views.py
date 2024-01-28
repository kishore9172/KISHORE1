from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        services=request.POST['service']
        obj=Datas()
        obj.Name=name
        obj.Phone=phone
        obj.Email=email
        obj.Services=services
        obj.save()
    return render(request,'home.html')
