from django.contrib import admin

# Register your models here.
from .models import User,Details 

admin.site.register(User)
admin.site.register(Details)