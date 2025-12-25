# local url i.e, app urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    # path('members/', views.members, name='members'),
    # path('members/details/<int:id>', views.details, name='details'),
    # path('testing/', views.testing, name='testing'),    
]