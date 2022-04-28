from tkinter.tix import AUTO
from django.db import models
from accounts.models import Member

# Create your models here.
class SchoolYear(models.Model):
    school_year = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.school_year}"

class ActivityLogs(models.Model):
    ADDED = 'Added'
    DELETED = 'Deleted'
    UPDATE = 'Update'
    CHANGE_CHOICES = [
        (ADDED, 'Added'),
        (DELETED, 'Deleted'),
        (UPDATE, 'Update')
    ]
    LMS = 'LMS'
    HR = 'HR'
    AIV = 'AIV'
    EVAL_CHOICES = [
        (LMS, 'LMS'),
        (HR, 'HR'),
        (AIV, 'AIV')
    ]
    member = member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_log = models.DateTimeField(auto_now=True)
    activity_log = models.CharField(max_length=200, choices=CHANGE_CHOICES)
    eval_log = models.CharField(max_length=200, choices=EVAL_CHOICES)
    def __str__(self):
        return f"{self.activity_log} evaluation on user {self.member} in {self.eval_log}. [{self.date_log}]"