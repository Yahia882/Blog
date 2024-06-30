from django.db import models
from django.utils.text import slugify
# Create your models here.

class Author (models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    def __str__(self):
        return self.tag_name
    
    def save(self,*args, **kwargs):
     self.tag_name = f'#{slugify(self.tag_name)}'
      
     super().save(*args, **kwargs)
    



class post_model(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to="images/")
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    brief = models.CharField(max_length=300,blank=True)
    slug = models.SlugField(unique=True,db_index=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return f"Title: {self.title} Author: {self.author}"

class comment_section(models.Model):
    Post = models.ForeignKey(post_model,on_delete=models.SET_NULL,null=True,blank=True)
    comment = models.CharField(max_length=300)