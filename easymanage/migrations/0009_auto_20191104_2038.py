# Generated by Django 2.0.5 on 2019-11-05 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0008_auto_20191104_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomstatus',
            name='room_availability',
            field=models.BooleanField(default=False),
        ),
    ]
