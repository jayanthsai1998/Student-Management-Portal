from django.contrib import admin

# Register your models here.

from onlineapp.models import *

admin.site.register(College)
admin.site.register(Student)
admin.site.register(MockTest1)