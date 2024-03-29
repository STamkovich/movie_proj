# Generated by Django 4.0.3 on 2022-04-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_alter_movie_budget_alter_movie_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=10)),
                ('last_name', models.CharField(default='', max_length=10)),
                ('director_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
