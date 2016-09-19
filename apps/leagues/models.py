from django.db import models

class LeagueManager(models.Manager):
	def new_league(self, data):
		errors = []

		if not data["name"]:
			errors.append("League name can not be blank")
		else:
			existing_league = self.filter(name=data["name"])
			
			if existing_league:
				errors.append("League name already in DB")

		if not data["sport"]:
			errors.append("Sport name can not be blank")

		response = {}

		if errors:
			response["errors"] = errors
			response["created"] = False
		else:
			new_league = self.create(name=data["name"], sport=data["sport"])
			
			response["created"] = True
			response["new_league"] = new_league

		return response

# Create your models here.
class League(models.Model):
	name = models.CharField(max_length=25)
	sport = models.CharField(max_length=25)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = LeagueManager()

class Team(models.Model):
	name = models.CharField(max_length=25)
	city = models.CharField(max_length=25)
	league = models.ForeignKey(League, related_name="teams")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)