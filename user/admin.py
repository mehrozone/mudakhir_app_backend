from django.contrib import admin

# Register your models here.
from user.models import *

admin.site.register(User)

admin.site.register(Feedback)
