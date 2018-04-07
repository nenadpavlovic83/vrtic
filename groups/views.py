from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def groupa(request):
    return render(request, 'grupa1.html')

def groupb(request):
    return render(request, 'grupa1.html')

def groupc(request):
    return render(request, 'grupa1.html')

def groupd(request):
    return render(request, 'grupa1.html')
