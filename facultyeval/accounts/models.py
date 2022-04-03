from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    """
    The member model is the faculty member that is also attached to user account.
    This will allow them to view their evaluations by visiting the web application.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profile_img")
    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}, {self.user.middle_name}"