from django.contrib import admin
from .models import Studentm
# Register your models here.


@admin.register(Studentm)
class StudentmAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']