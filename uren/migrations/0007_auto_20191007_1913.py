# Generated by Django 2.2.1 on 2019-10-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uren', '0006_auto_20191007_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecthours',
            name='week',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projecthours',
            name='year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
