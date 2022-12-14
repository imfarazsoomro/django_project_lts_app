# Generated by Django 4.0.5 on 2022-08-01 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='due_date',
            field=models.DateField(default=datetime.date(2022, 8, 1)),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='price',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('request', 'Open Request'), ('offer', 'Received Offer'), ('agreement', 'Agreement')], default='request', max_length=50),
        ),
    ]
