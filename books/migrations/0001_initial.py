# Generated by Django 3.1 on 2020-09-27 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('urlToImage', models.CharField(max_length=120)),
                ('url', models.CharField(max_length=120)),
            ],
        ),
    ]
