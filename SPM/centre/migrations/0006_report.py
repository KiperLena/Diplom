# Generated by Django 4.2.3 on 2023-07-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0005_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=200, verbose_name='Месторождение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('area', models.ManyToManyField(blank=True, to='centre.area', verbose_name='Лицензионный участок')),
                ('type', models.ManyToManyField(blank=True, to='centre.type', verbose_name='Вид работ')),
            ],
        ),
    ]
