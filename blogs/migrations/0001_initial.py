# Generated by Django 3.1 on 2020-09-27 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=15)),
                ('slug', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
