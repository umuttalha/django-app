from pyexpat import model
from django.db import models
from matplotlib.pyplot import title

import informations

# Create your models here.

class Information(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    information_file = models.FileField(blank=True,null=True,verbose_name="Add file")

    def __str__(self):
        return self.title