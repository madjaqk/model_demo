from django.shortcuts import render, redirect
from django.contrib import messages
from .models import League, Team

# Create your views here.
def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def show(request, id):
	this_league = League.objects.get(id=id)
	context = {
		"league": this_league,
		# "teams": Team.objects.filter(league=this_league)
	}
	return render(request, "leagues/show.html", context)

def create_league(request):
	if request.method=="POST":
		res = League.objects.new_league(request.POST)

		if res["created"]:
			messages.success(request, "{} successfully created".format(res["new_league"].name))
			# messages.success(request, res["new_league"].name + " successfully created")
		else:
			for error in res["errors"]:
				messages.error(request, error)

	return redirect("/")

def create_team(request):
	if request.method=="POST":
		new_team = Team()
		new_team.name = request.POST["name"]
		new_team.city = request.POST["city"]
		new_team.league = League.objects.get(id=request.POST["league_id"])
		new_team.save()

	return redirect("/")