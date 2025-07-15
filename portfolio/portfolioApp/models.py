from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    textarea = models.TextField(max_length=500)
    
class Works(models.Model):
    title = models.CharField(max_length=100)
    programing_lang_used = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='works/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title