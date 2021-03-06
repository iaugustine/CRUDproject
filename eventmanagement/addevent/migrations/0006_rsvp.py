# Generated by Django 3.0.3 on 2020-05-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addevent', '0005_auto_20200514_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('no_ticket', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='addevent.Events')),
            ],
        ),
    ]
