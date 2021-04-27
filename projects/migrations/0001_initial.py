# Generated by Django 3.2rc1 on 2021-04-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('header', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('image', models.FilePathField(blank=True, default='default_user.jpg', null=True, path='static/images/user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('short', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('technology', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.FilePathField(blank=True, default='default_user.png', null=True, path='static/images/projects')),
                ('url', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('demo', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('slug', models.SlugField(max_length=500, unique=True)),
            ],
        ),
    ]
