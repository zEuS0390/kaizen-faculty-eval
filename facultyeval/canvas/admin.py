from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Evaluation)
admin.site.register(Result)
admin.site.register(Criteria)
admin.site.register(CriteriaScore)