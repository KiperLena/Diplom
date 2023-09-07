from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя Фамилия")
    profession = models.CharField(max_length=100, blank=True, null=True, verbose_name="Должность")
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Электронная почта")
    username = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя на сайте")
    phone = models.CharField(max_length=60, blank=True, null=True, verbose_name="Телефон")
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отдел, направление")
    info = models.TextField(blank=True, null=True, verbose_name="Информация о пользователе")
    account_image = models.ImageField(upload_to="accounts/", default="accounts/user-default.png")


    def __str__(self):
        return self.username

    class Meta: #служебный класс
        verbose_name = "профиль пользователя" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Профили пользователей"












