# Generated by Django 5.0.4 on 2024-05-07 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=datetime.date(2002, 1, 1), verbose_name='发布时间'),
        ),
    ]
