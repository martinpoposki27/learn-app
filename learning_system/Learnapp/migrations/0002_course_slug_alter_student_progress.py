# Generated by Django 4.0.4 on 2022-08-12 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learnapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='progress',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
