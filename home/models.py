from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
import time
import datetime
# Create your models here.

class UserProfile(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField(blank=False,null=False,primary_key=True)
    website = models.URLField(blank=True)
    current_q_no=models.CharField(default="1" ,max_length=30)
    panilty=models.CharField(default="0",max_length=30 )
    lst=models.IntegerField(default=0)
    def __unicode__(self):
        return self.username
class Question_ans_key(models.Model):
	q_no=models.CharField(max_length=30)
	ans=models.CharField(max_length=30)
	key=models.CharField(max_length=30)
	def __str__(self):
		return self.ans
class Submission(models.Model):
	user=models.ForeignKey(UserProfile)
	time=models.DateTimeField(default=datetime.datetime.now())
	qno=models.CharField(max_length=30)
	def __str__(self):
		return self.user.username