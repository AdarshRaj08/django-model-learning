from django.db import models


# 1. Abstract Base class
# 2. Multi-table Inheritance
# 3. Proxy models


# ################### Abstract Base Class ##################

# Abstract base classes are useful when you want to put some common information into a number of other models.
# you write your base class and put abstract=True in the Meta class.

# This model will then not be used to create any database table. Instead, when it is used as a base class for 
#   other models, its fields willl be added to those of the child class.

# It does not generate a database table or have a manager, and cannot be instantiated or saved directly.

# fields inherited from abstract base classes can be overridden with another field or value, or be remoed with None.

# NOTE -> Meta Inheritance 
#         when an abstract base class is created, django makes any meta inner class you declared
#         in the base class available as an attribute.

# if a child class doesn't declare it own Meta class, it will inherit the parent's Meta.
# django do abstract=false before inheriting meta class to the child (if you have to do astract then do abstract=True)


# Create your models here.

# here we don't want to make the table for the commoninfo model so we put into the abstract class
class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True


class Student(CommonInfo):
    fees = models.IntegerField()
    # here let's say student not require date field then 
    date = None

class Teacher(CommonInfo):
    salary = models.IntegerField()
    date = None

class Contractor(CommonInfo):
    date = models.DateTimeField()     # here override date field
    payment = models.IntegerField()
    



# ######################### Multi-table Inheritance #####################################

# Multi-table inheritance is useful when you need to extend existing models while maintaining separate tables for each model in the hierarchy. 


# in this inheritance each model have their own database table, which means base class and child class their own table.
# The inheritance relationship introduces links between the child model and each of its parents (via an automaticall-created OneToOneField)

# when we fill the data then the data will go to their own table
# dono table foreign key se connected hota hai 
# here when we fill data in student2 table then the value of cname,city will go in their own field
# when we delete the data of the student2 table then the data of that foregin key willl delete from the examcentre 

class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class Student2(ExamCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()




# ######################### Proxy-Model ##########################################3

# Proxy models in Django are a way to create a different Python-level behavior for an existing model without creating a separate table in the database.
#  They allow you to add or change the behavior of a model without altering its fields or creating a new database schema.

# A proxy model must inherit from exactly one non-abstract model class.
# You can't inherit from multiple non-abstract models as the proxy model doesn't provide any connection b/w the rows in the different database tables

# A proxy model can inherit from any number of abstract class, providing they don't define any model fields.
# A proxy model may also inherit form any number of proxy models that share a common non-abstract parent class.

# if you don't specify any models managers on a proxy odel, it inherits the managers from its model parents.
# if you define a manager on the proxy model, it will become the default, although any mangers defined on the parent classes will still be available.


# here two model but only one table is created in database
# so when we insert data in any model data will go 


class ExamCenter2(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class MyExamCenter(ExamCenter2):
    class Meta:
        proxy = True
        ordering = ['-id']