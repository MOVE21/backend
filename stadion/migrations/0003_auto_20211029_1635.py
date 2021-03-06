# Generated by Django 3.2.8 on 2021-10-29 13:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20211029_1635'),
        ('team', '0003_alter_team_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stadion', '0002_auto_20211029_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stadion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stadion',
            name='matches',
            field=models.ManyToManyField(null=True, to='matches.Match'),
        ),
        migrations.AlterField(
            model_name='stadion',
            name='players',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stadion',
            name='teams',
            field=models.ManyToManyField(null=True, to='team.Team'),
        ),
    ]
