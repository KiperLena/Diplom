from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User #какой класс подключила
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2'] #поля которые подключаем
        labels = {
            'first_name': 'Введите Имя',
            'last_name': 'Введите Фамилию',
            'username': 'Имя пользователя',
        }











