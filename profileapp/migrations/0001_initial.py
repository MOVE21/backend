# Generated by Django 3.1.7 on 2021-10-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('midname', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('descr', models.TextField()),
            ],
        ),
    ]
