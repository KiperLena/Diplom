from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.centre, name='centre'),
    path('index/', views.index, name='index'),
    path('account/', include('users.urls')),
    path('area/<str:pk>/', views.area, name='area'),
    path('biblioteka/', views.old_doc, name='old_doc'),
    path('create-report/', views.create_report, name='create-report'),
]