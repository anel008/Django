from django.contrib import admin

# Register your models here.
from .models import Department,Doctor,Booking

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Booking)