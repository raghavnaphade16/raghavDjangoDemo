from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Raghav N'})

def add(request):
      #  no1=request.GET.get('no1','default')
      #  no2=request.GET.get('no2','default')
    no1=request.POST['no1']
    no2=request.POST['no2']
    print("No1 is"+no1+"No 2 is"+no2)
    res=int(no1)+int(no2)

    return render(request,'result.html',{'result':res})

