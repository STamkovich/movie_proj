# Generated by Django 4.0.3 on 2022-04-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=10)),
                ('last_name', models.CharField(default='', max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movie_app.actor'),
        ),
    ]
