from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def accounts(request, pk):
    prof = Account.objects.get(id=pk)

    context = {
        'account': prof,
    }
    return render(request, 'users/account.html', context)


def login_user(request): #авторизация
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Такого пользователя не существует!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Имя или пароль некорректны!")

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "Пользователь разлогинился!")
    return redirect('login')


def register_user(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Пользователь успешно зарегистрирован!")

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)
