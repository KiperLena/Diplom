# Generated by Django 4.2.3 on 2023-09-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0017_remove_bid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='area',
            field=models.ManyToManyField(blank=True, to='centre.area', verbose_name='Лицензионный участок'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='title',
        ),
        migrations.AddField(
            model_name='bid',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название задачи'),
        ),
    ]