from turtle import title
from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(max_length= 250)
    content = models.TextField(null= True)
    auth = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add= True )
    updated = models.DateTimeField(auto_now_add= True)
    published = models.BooleanField()



    def __str__(self):  
        return self.title
