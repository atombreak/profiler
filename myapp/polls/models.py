from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  text = models.TextField(max_length=400)
  slug = models.SlugField()
  
  def __str__(self):
    return self.title
  