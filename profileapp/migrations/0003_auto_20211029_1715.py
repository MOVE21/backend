# Generated by Django 3.2.8 on 2021-10-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='descr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='midname',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.TextField(null=True),
        ),
    ]
