# Generated by Django 3.2.8 on 2021-10-30 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('x', models.FloatField(default=0)),
                ('y', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileapp.avatar'),
        ),
    ]
