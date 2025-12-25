# main url file ka jaisa sab hota bas one thing is that
# ham log yaha views imort karta app ka

from django.contrib import admin
from django.urls import include, path
from home import views



urlpatterns = [
    

    # to show the view function
    path('', views.home, name='home')
]