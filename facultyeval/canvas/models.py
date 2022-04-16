from django.db import models
from accounts.models import Member
from administrator.models import SchoolYear

# Create your models here.
class MGRating(models.Model):
    FIRST_SEM = '1st Sem'
    SECOND_SEM = '2nd Sem'
    SEMESTER_CHOICES = [
        (FIRST_SEM, 'First Semester'),
        (SECOND_SEM, 'Second Semester')
    ]
    MODULAR_1 = 'MG1'
    MODULAR_2 = 'MG2'
    MODULAR_3 = 'MG3'
    MODULAR_4 = 'MG4'
    MG_CHOICES = [
        (MODULAR_1, 'Modular Group 1'),
        (MODULAR_2 , 'Modular Group 2'),
        (MODULAR_3, 'Modular Group 3'),
        (MODULAR_4, 'Modular Group 4')
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    group_title = models.CharField(max_length=200, choices=MG_CHOICES, default=MODULAR_1)
    semester = models.CharField(max_length=200, choices=SEMESTER_CHOICES, default=FIRST_SEM)
    part1 = models.FloatField()
    part2 = models.FloatField()
    final = models.FloatField()
    remarks = models.CharField(max_length=400)
    def __str__(self):
        return f"{self.member} - {self.school_year} - {self.semester} - {self.group_title}"