from django.contrib import admin
from profiles_api import models
from .models import UserProfile

admin.site.register(UserProfile)
