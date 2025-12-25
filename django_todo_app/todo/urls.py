from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # Define a route
    path('todo/create', views.create_todo, name='create_todo'),
]
