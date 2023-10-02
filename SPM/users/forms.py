from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Account


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


class CurrentAccount(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'profession', 'email', 'username', 'phone', 'department', 'info', 'account_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-report'})
            # field.widget.attrs['class'] = 'fadeIn third'









