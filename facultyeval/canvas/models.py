from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.middle_name}"

class Course(models.Model):
    course_title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.course_code} - {self.course_title}"

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.section_name} - {self.course}"

class Result(models.Model):
    faculty_member = models.ForeignKey(Member, on_delete=models.CASCADE)
    faculty_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faculty_course} - {self.faculty_member}"

class Evaluation(models.Model):
    evaluation_title = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f"{self.evaluation_title}"

class Criteria(models.Model):
    faculty_evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    criteria_title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.faculty_evaluation} - {self.criteria_title}"

class CriteriaScore(models.Model):
    evaluation_result = models.ForeignKey(Result, on_delete=models.CASCADE)
    evalutation_criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.evaluation_result} - {self.evalutation_criteria} - {self.score}"