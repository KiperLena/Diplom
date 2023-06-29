# Generated by Django 3.0.14 on 2023-06-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='square',
            new_name='num',
        ),
        migrations.RemoveField(
            model_name='area',
            name='area_image',
        ),
        migrations.RemoveField(
            model_name='area',
            name='description',
        ),
        migrations.AddField(
            model_name='area',
            name='otvod',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='region',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='seria',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='start',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='stop',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
