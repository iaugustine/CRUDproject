# Generated by Django 3.0.3 on 2020-05-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addevent', '0002_auto_20200514_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='e_date',
            field=models.DateField(),
        ),
    ]
