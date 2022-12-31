from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    Slug = models.SlugField(max_length=225)

    def __str__(self):
       return self.title


