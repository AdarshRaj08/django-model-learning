from django.db import models
from .managers import CustomManager

# A manager is the interface through which database query are provided to Django models.
# At least one Manager exists for every model in a Django application.
# Model manager is used to interact with database.

# by default , Django adds a Manager with the name objects to every Django model class.


# Create your models here.
class Studentm(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # here like this you can change your manager name
    # adarsh = models.Manager()

    # here we importing custom manager from the managers.py
    adarsh = CustomManager()

    # here if we want that objects will run as well then also define objects after assigning custom both will work
    objects = models.Manager()
