# Generated by Django 3.0.8 on 2020-09-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200904_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessdetails',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]