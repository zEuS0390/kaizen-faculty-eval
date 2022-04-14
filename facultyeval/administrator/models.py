from django.db import models

# Create your models here.
class SchoolYear(models.Model):
    school_year = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.school_year}"