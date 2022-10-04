from django.contrib import admin
from .models import Issue

# Register your models here.
# It's not required to register a model that doesnt need to be accessed by the admin. 
admin.site.register(Issue)