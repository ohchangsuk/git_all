# Generated by Django 3.0.1 on 2020-01-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table1',
            name='img',
            field=models.BinaryField(null=True),
        ),
    ]
