# Generated by Django 4.2.5 on 2024-01-19 10:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userachievement',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userachievement',
            name='event_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.event'),
        ),
    ]
