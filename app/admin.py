from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(State)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(Tourist)
