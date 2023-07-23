# Generated by Django 4.2.3 on 2023-07-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0004_type_delete_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
    ]