from . import views
from django.urls import path
from django.urls.resolvers import URLPattern


app_name = "student"


urlpatterns = [
    path("home", views.index, name="index"),
    path("submit", views.get_topic, name="topic"),
    path("graph", views.index, name="index"),
    path("subtopic", views.get_subtopic, name="subtopic")

]
