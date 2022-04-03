from django.db import models

# Create your models here.
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