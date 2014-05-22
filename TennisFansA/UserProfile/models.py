from django.db import models
from Account.models import MyUser


class Profile(models.Model):
	LEVEL=(('1','1'),('1.5','1.5'),('2','2'),('2.5','2.5'),('3','3'),('3.5','3.5'),('4','4'),('4.5','4.5'),('5','5'),('5.5','5.5'),('6','6'),('6.5','6.5'),('7','7'),('7.5','7.5'),)
	GENDER=(('0','male'),('1','female'))
	CITY=(('1','Suzhou'),('2','Beijing'),('3','Shanghai'))
	user = models.OneToOneField(MyUser,primary_key=True)
	username = models.CharField(max_length = 100)
	level = models.CharField(max_length=15, choices=LEVEL, default='3')
	phone = models.CharField(max_length=11)
#	province = models.CharField(max_length=100)
	gender = models.CharField(max_length=2, choices=GENDER)
	city = models.CharField(max_length=3,choices=CITY, default='1')
	
MyUser.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
