# Generated by Django 3.0.14 on 2023-06-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
                ('area_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='centre/%Y')),
                ('square', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]