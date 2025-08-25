from django.contrib import admin
from factors.models import Activity
# Register your models here.

@admin.register(Activity)
class Factors(admin.ModelAdmin):
    list_display = ("id",'user','category','co2_emission')