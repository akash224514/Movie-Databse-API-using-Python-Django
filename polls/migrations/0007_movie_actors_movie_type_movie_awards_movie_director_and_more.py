# Generated by Django 4.0.4 on 2022-05-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Actors',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='Type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='awards',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='writer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
