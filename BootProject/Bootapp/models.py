from django.db import models

# Create your models here.
class Bootcamp_candidate(models.Model):
    Name = models.CharField(max_length=20)
    ID = models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
