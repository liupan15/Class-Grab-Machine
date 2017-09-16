from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
    id1 = models.CharField(max_length = 20);
    id2 = models.CharField(max_length = 10);
#    time = models.CharField(max_length = 20);
#    student = models.ManyToManyField(User, related_name = 'student_id');

    
class UserPlus(models.Model):
    userid = models.CharField(max_length = 20);
   # password = models.CharField(max_length = 20);  # 最长不超过20
   # online = models.IntegerField();
    user = models.OneToOneField(User);
    
    lessons = models.ManyToManyField(Lesson);
    
    

