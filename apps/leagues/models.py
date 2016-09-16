from django.db import models

# Create your models here.
class League(models.Model):
	name = models.CharField(max_length=25)
	sport = models.CharField(max_length=25)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
	name = models.CharField(max_length=25)
	city = models.CharField(max_length=25)
	league = models.ForeignKey(League, related_name="teams")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)