from django.urls import path
from . import views

urlpatterns = [
    path('', views.centre, name='centre'),
    path('index/', views.index, name='index'),
    path('area/<str:pk>/', views.area, name='area'),
    path('biblioteka/', views.old_doc, name='old_doc'),
    path('create-report/', views.create_report, name='create-report'),



]