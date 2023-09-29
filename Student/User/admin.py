from django.contrib import admin

# Register your models here.
from .models import Courses,Course_details,Account



admin.site.register(Courses)
admin.site.register(Course_details)
admin.site.register(Account)