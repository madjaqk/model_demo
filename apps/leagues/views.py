from django.shortcuts import render, redirect
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
		League.objects.create(name=request.POST["name"], sport=request.POST["sport"])

	return redirect("/")

def create_team(request):
	if request.method=="POST":
		new_team = Team()
		new_team.name = request.POST["name"]
		new_team.city = request.POST["city"]
		new_team.league = League.objects.get(id=request.POST["league_id"])
		new_team.save()

	return redirect("/")