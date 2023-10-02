from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CurrentAccount
from .utils import paginate_profiles, search_profiles
from django.db.models import Q #для поиска


def profiles(request): #все аккаунты пользователей, поиск
    prof, search_query = search_profiles(request)
    custom_range, prof = paginate_profiles(request, prof, 4)
    context = {
        'profiles': prof,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'users/index.html', context)


def user_profile(request, pk): #профиль пользователя
    prof = Account.objects.get(id=pk)
    context = {
        'profile': prof,
    }
    return render(request, 'users/profile.html', context)


def login_user(request):  # авторизация
    if request.user.is_authenticated:
        return redirect('info')

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
            return redirect('centre')
        else:
            messages.error(request, "Имя или пароль некорректны!")

    return render(request, 'users/login_register.html')


def logout_user(request): #разлогиниться
    logout(request)
    messages.info(request, "Пользователь разлогинился!")
    return redirect('login')


def register_user(request): #Регистрация
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Пользователь успешно зарегистрирован!")
            login(request, user)
            return redirect('centre')
        else:
            messages.error(request, "При регистрации произошла ошибка!")

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)


def user_account(request): #редактирование своего аккаунта
    profile = request.user.account
    form = CurrentAccount(instance=profile)

    if request.method == 'POST':
        form = CurrentAccount(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_account')
    context = {
        'form': form,
    }
    return render(request, 'users/user_account.html', context)


