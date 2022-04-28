from django.db import models
from accounts.models import Member
from administrator.models import SchoolYear

# Create your models here.
class HRRating(models.Model):
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

class HRCriterion(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.title}"

class HRCriterionScores(models.Model):
    hrrating = models.ForeignKey(HRRating, on_delete=models.CASCADE)
    hrcriterion = models.ForeignKey(HRCriterion, on_delete=models.CASCADE)
    program_chair_score = models.FloatField()
    student_score = models.FloatField()
    average_score = models.FloatField()
    remarks = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.hrrating} - {self.hrcriterion} - {self.program_chair_score} - {self.student_score} - {self.average_score} - {self.remarks}"