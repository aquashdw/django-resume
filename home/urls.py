from django.urls import path

from home import views


app_name = "resume"
urlpatterns = [
    path("", views.index, name="home")
]
