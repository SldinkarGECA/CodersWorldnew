# Generated by Django 3.1.1 on 2020-09-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200924_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseUrl',
            field=models.CharField(max_length=200),
        ),
    ]