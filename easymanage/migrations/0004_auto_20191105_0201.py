# Generated by Django 2.0.5 on 2019-11-05 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0003_auto_20191105_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_DOB',
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(auto_created=True, max_length=6, primary_key=True, serialize=False),
        ),
    ]
