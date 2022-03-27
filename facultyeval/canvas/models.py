from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    """
    The member model is the faculty member that is also attached to user account.
    This will allow them to view their evaluations by visiting the web application.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.middle_name}"

class Course(models.Model):
    """
    The course model will specify the area of performance of the faculty member.
    """
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.code} - {self.title}"

class Section(models.Model):
    """
    The section model determines the specific class in the course that
    the evaluation of a faculty member has been gathered.
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.section_name} - {self.course}"

class Result(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.course} - {self.member}"

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