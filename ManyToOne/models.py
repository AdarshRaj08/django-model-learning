from django.db import models
from django.contrib.auth.models import User

# Many To One - One user can do multiple post (one row of a table can linked with the multiple fields)



# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.PROTECT)

    # here when we delete user there post will be there but on that column where they connect Null will be fillout
    # user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()
