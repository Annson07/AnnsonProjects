from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.


def demo(request):
       obj=Place.objects.all()
       obj1=Team.objects.all()
       return render(request,"index.html",{'result':obj,'team':obj1})

# def addition(request):
#        x=int(request.GET['num1'])
#        y=int(request.GET['num2'])
#        res1=x+y
#
#        return render(request,"result.html",{'result1':res1})
#
# def substraction(request):
#        x=int(request.GET['num1'])
#        y=int(request.GET['num2'])
#        res2=x-y
#        return render(request,"result.html",{'result2':res2})




#
# def contacts(request):
#        return HttpResponse("HELLO I AM CONTACT")