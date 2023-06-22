from django.urls import path
from . import views

urlpatterns = [
    path('', views.centre, name='centre'),
    path('area/<str:pk>/', views.area, name='area'),
]