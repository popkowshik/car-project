from django.urls import path 
from . import views


urlpatterns = [
    path('home_cars/',views.home_cars),
    path('one_car/<int:id>/',views.one_car,name='power'),
]