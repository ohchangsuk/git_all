# Generated by Django 3.0.1 on 2020-01-02 01:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table1',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=50)),
                ('hit', models.IntegerField()),
                ('regdate', models.DateField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
