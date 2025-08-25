from django.contrib import admin
from users.models import User
# Register your models here.
@admin.register(User)
class Users(admin.ModelAdmin):
    list_display = ("id","username","password")