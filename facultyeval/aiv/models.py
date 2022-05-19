from django.db import models
from accounts.models import Member
from administrator.models import SchoolYear

# Create your models here.
class AIVRating(models.Model):
    FIRST_SEM = '1st-Sem'
    SECOND_SEM = '2nd-Sem'
    SEMESTER_CHOICES = [
        (FIRST_SEM, 'First Semester'),
        (SECOND_SEM, 'Second Semester')
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    semester = models.CharField(max_length=200, choices=SEMESTER_CHOICES, default=FIRST_SEM)
    def __str__(self):
        return f"{self.member} - {self.school_year} - {self.semester}"

class AIVCriterion(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.title}"

class AIVCriterionScores(models.Model):
    aivrating = models.ForeignKey(AIVRating, on_delete=models.CASCADE)
    aivcriterion = models.ForeignKey(AIVCriterion, on_delete=models.CASCADE)
    first_visit = models.FloatField(blank=True, null=True)
    second_visit = models.FloatField(blank=True, null=True)
    average_score = models.FloatField(blank=True , null=True)
    remarks = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.aivrating} - {self.aivcriterion} - {self.first_visit} - {self.second_visit} - {self.average_score} - {self.remarks}"