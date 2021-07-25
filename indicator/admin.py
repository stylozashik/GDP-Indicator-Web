from django.contrib import admin
from .models import YearlyGDP

# Unregister group section
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

# Change admin site header
admin.site.site_header = 'Dashboard'

# Register your models here.
admin.site.register(YearlyGDP)