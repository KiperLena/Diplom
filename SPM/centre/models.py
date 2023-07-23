from django.db import models


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
    field = models.CharField(max_length=200, verbose_name="Месторождение")
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