# Generated by Django 4.0.4 on 2022-05-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
