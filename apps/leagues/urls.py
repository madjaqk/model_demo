from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^league/(?P<id>\d+)", views.show, name="show"),
	url(r"^create_league", views.create_league, name="create_league"),
	url(r"^create_team", views.create_team, name="create_team"),
]