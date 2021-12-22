# Generated by Django 3.2.4 on 2021-07-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hrplatform', '0003_auto_20210710_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio_store1',
            old_name='fillerwords',
            new_name='Fillerwords',
        ),
        migrations.RenameField(
            model_name='audio_store1',
            old_name='sensitivewords',
            new_name='Sensitivewords',
        ),
        migrations.RenameField(
            model_name='audio_store1',
            old_name='spotwords',
            new_name='Spotwords',
        ),
        migrations.AddField(
            model_name='audio_store1',
            name='freq',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audio_store1',
            name='meanpitch',
            field=models.CharField(default='', max_length=120),
        ),
    ]
