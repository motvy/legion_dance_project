# Generated by Django 4.2.5 on 2023-09-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_team_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='exp',
            field=models.IntegerField(default=0),
        ),
    ]