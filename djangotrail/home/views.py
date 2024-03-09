from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctor

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):

    return render(request, 'contact.html')
def doctor(request):
    doc = {'doct': Doctor.objects.all()}

    return render(request,'doctor.html',doc)
def booking(request):

    return render(request, 'booking.html')
def department(request):

    depp= Department.objects.all()
    x = {
        'dep':depp
        }
     
    return render(request,'department.html',x)