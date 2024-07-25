from django.contrib import admin
from .models import Student,Teacher,Contractor,ExamCenter,Student2,ExamCenter2,MyExamCenter

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','date','salary']


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','date','payment']



# ##################### Multi-table inheritance #############################

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']


@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id','cname','city','name','roll']


# #################### Proxy Model #########################################


@admin.register(ExamCenter2)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']
