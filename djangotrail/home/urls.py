from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index,name= "home"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    path('doctor', views.doctor,name = "doctors"),
    path('booking', views.booking,name = "booking"),
    path('department', views.department,name = "department")
]
