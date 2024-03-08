from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    person = {
        'Name' : 'Anel babu',
        'age' : 23,

    }
    return render(request, 'index.html',person)
def about(request):
    number = {'num1': 1}

    return render(request, 'about.html',number)
def contact(request):
    return render(request, 'contact.html')
def doctor(request):
    return render(request, 'doctor.html')
def booking(request):
    return render(request, 'booking.html')
def department(request):
    return render(request,'department.html')