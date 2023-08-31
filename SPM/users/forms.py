from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'fadeIn third'


    class Meta:
        model = User #какой класс подключила
        fields = ['first_name', 'last_name', 'username'] #поля которые подключаем
        labels = {
            'first_name': 'Введите Имя',
            'last_name': 'Введите Фамилию',
            'username': 'Имя пользователя',
        }











