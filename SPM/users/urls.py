from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>/', views.accounts, name="accounts"),


    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
]