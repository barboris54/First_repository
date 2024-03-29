from django.db import models

class My_skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='my_skills/images/')
    url = models.URLField(blank=True)
