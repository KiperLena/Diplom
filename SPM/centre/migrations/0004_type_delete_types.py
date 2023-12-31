# Generated by Django 4.2.3 on 2023-07-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0003_types_alter_area_options_alter_area_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Вид работ',
                'verbose_name_plural': 'Виды работ',
            },
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]
