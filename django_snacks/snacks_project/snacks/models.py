from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class items(models.Model):
    name = models.CharField(max_length= 40)
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)

