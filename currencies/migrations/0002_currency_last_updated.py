# Generated by Django 3.2 on 2021-12-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
