# Generated by Django 4.2.3 on 2023-07-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0007_rename_area_report_title_report_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Отчет', 'verbose_name_plural': 'Отчеты'},
        ),
        migrations.AddField(
            model_name='report',
            name='name',
            field=models.ManyToManyField(blank=True, to='centre.group', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
    ]
