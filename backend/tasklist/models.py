from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):  #this function allows us to see the title and author of the post on admin page
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return f'/{self.pk}/'
