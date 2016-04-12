from django.contrib import admin
from home.models import UserProfile
from home.models import Question_ans_key
from home.models import Submission
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Question_ans_key)
admin.site.register(Submission)