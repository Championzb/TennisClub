from django.db import models
from Account.models import MyUser

class LeagueMatch(models.Model):

	CITY=(('1','Suzhou'),('2','Beijing'),('3','Shanghai'))

	name = models.CharField(max_length=100)
	start_date = models.DateField()
	finish_date = models.DateField()
	city = models.CharField(max_length=3,choices=CITY, default='1')
	player = models.ManyToManyField(MyUser,blank=True)

	

class Match(models.Model):
	leagueMatch = models.ForeignKey(LeagueMatch)
	date = models.DateField()
	player1 = models.ForeignKey(MyUser,related_name='player1')
	player2 = models.ForeignKey(MyUser,related_name='player2')
	score = models.CharField(max_length = 200)
