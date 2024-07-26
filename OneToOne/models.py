from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# here when we delete page then no effect on user
# when we delete user then the page which is created by the user will also be deleted in (CASCADE)

# when on_delete=models.PROTECT then we can't delte the user which is created the page
# if user don't created page then it's okk you can delte them
# you can delte page like normal

# here you can limit the choices of page creating to the specific member

class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    # on_delete=models.PROTECT
    # user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)

    # limit_choices_to={'is_staff':True}
    # user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True,
    #                             limit_choices_to={'is_staff':True})


    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()




# ################################### One2One Reverse Relation #####################################33

# upper when page delete nothing happen to the user but heere we want that when we delete the page user will also delete