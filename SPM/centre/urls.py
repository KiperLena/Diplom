from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('licea-area', views.licea_area, name='licea_area'),
    path('', views.centre, name='centre'),
    path('profiles/', include('users.urls')),
    path('area/<str:pk>/', views.area, name='area'),
    path('biblioteka/', views.old_doc, name='old_doc'),
    path('create-report/', views.create_report, name='create-report'),
    path('create-bid/', views.create_bid, name='create_bid'),
    path('current-bid/', views.current_bid, name='current_bid'),
    path('bid/<int:bid_pk>/', views.viewbid, name='viewbid'),
    path('bid/<int:bid_pk>/complete/', views.completebid, name='completebid'),
    path('bid/<int:bid_pk>/delete/', views.deletebid, name='deletebid'),
    path('completed/', views.completedbid, name='completedbid'),
]