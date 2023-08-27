from django.db import models
from users.models import Account


class Area(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название ЛУ")
    seria = models.CharField(max_length=20, blank=True, null=True, verbose_name="Серия")
    num = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер")
    type = models.CharField(max_length=20, blank=True, null=True, verbose_name="Тип")
    otvod = models.CharField(max_length=20, blank=True, null=True, verbose_name="Отвод")
    start = models.CharField(max_length=20, blank=True, null=True, verbose_name="Выдали")
    stop = models.CharField(max_length=20, blank=True, null=True, verbose_name="Окончание")
    region = models.CharField(max_length=20, blank=True, null=True, verbose_name="Регион")

    def __str__(self):
        return self.title

    class Meta: #служебный класс
        verbose_name = "Лицензионный участок" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Лицензионные участки"


class Type(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta: #служебный класс
        verbose_name = "Вид работ" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Виды работ"


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta: #служебный класс
        verbose_name = "Отдел" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Отделы"


class Report(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    field = models.CharField(max_length=60, verbose_name="Месторождение")
    title = models.ManyToManyField('Area', blank=True, verbose_name="Лицензионный участок")
    type = models.ManyToManyField('Type', blank=True, verbose_name="Вид работ")
    description = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    name = models.ManyToManyField('Group', blank=True, verbose_name="Отдел")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self):
        return self.field

    class Meta: #служебный класс
        verbose_name = "Отчет" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Отчеты"


class Department1(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    post = models.CharField(max_length=100, verbose_name="Должность")
    telephone = models.CharField(max_length=20, verbose_name="Номер телефона рабочий")
    mobile_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Мобильный телефон")
    email = models.EmailField(max_length=60, blank=True, null=True, verbose_name="Электронная почта")
    office = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер кабинета")
    name = models.ManyToManyField('Group', blank=True, verbose_name="Отдел")


    def __str__(self):
        return self.full_name

    class Meta: #служебный класс
        verbose_name = "список сотрудников ОПМ" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Списки сотрудников ОПМ"


class Department2(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    post = models.CharField(max_length=100, verbose_name="Должность")
    telephone = models.CharField(max_length=20, verbose_name="Номер телефона рабочий")
    mobile_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Мобильный телефон")
    email = models.EmailField(max_length=60, blank=True, null=True, verbose_name="Электронная почта")
    office = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер кабинета")
    name = models.ManyToManyField('Group', blank=True, verbose_name="Отдел")


    def __str__(self):
        return self.full_name

    class Meta: #служебный класс
        verbose_name = "список сотрудников ОСМ" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Списки сотрудников ОСМ"

class Directorate(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    post = models.CharField(max_length=100, verbose_name="Должность")
    telephone = models.CharField(max_length=20, verbose_name="Номер телефона рабочий")
    mobile_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Мобильный телефон")
    email = models.EmailField(max_length=60, blank=True, null=True, verbose_name="Электронная почта")
    office = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер кабинета")
    image = models.ImageField(upload_to="accounts/", default="accounts/user-default.png")

    def __str__(self):
        return self.full_name

    class Meta: #служебный класс
        verbose_name = "список руководителей" # перевод на русский на странице админа в единственом числе
        verbose_name_plural = "Списки руководителей"