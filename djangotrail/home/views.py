from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctor
from .forms import Bookingform

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
    form = Bookingform()
    dict_form = {'form' : form }

    return render(request, 'booking.html',dict_form)
def department(request):

    depp= Department.objects.all()
    x = {
        'dep':depp
        }

    return render(request,'department.html',x)