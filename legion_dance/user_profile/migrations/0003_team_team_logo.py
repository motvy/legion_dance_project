# Generated by Django 4.2.5 on 2023-09-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_user_team_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_logo',
            field=models.ImageField(blank=True, null=True, upload_to='team_images'),
        ),
    ]