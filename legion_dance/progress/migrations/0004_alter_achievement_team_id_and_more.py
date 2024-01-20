# Generated by Django 4.2.5 on 2024-01-20 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_author_id_alter_teamevent_event_id_and_more'),
        ('user_profile', '0005_alter_user_team_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('progress', '0003_achievement_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='team_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.team'),
        ),
        migrations.AlterField(
            model_name='userachievement',
            name='achievement_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='progress.achievement'),
        ),
        migrations.AlterField(
            model_name='userachievement',
            name='event_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
        migrations.AlterField(
            model_name='userachievement',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
