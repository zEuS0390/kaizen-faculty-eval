from django.db import models
from accounts.models import Member
from administrator.models import Course, Section

# Create your models here.
class Result(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.course} - {self.section} - {self.member}"

class Evaluation(models.Model):
    title = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f"{self.title}"

class Criteria(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.evaluation} - {self.title}"

class Item(models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.criteria} - {self.description}"

class CriteriaScore(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.result} - {self.item.description} - {self.score}"