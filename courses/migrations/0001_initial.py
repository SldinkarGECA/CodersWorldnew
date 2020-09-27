# Generated by Django 3.1.1 on 2020-09-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=50)),
                ('courseImage', models.ImageField(upload_to='images/')),
                ('courseUrl', models.CharField(max_length=120)),
                ('courseDescription', models.CharField(max_length=1200)),
                ('courseCategory', models.CharField(max_length=120)),
            ],
        ),
    ]
