# Generated by Django 3.2.8 on 2021-10-30 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0004_auto_20211029_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminvite',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invites.status'),
        ),
        migrations.AddField(
            model_name='userinvite',
            name='descr',
            field=models.TextField(null=True),
        ),
    ]
