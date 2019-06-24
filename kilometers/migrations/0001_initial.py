# Generated by Django 2.2.1 on 2019-06-24 09:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('zip_code', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{4}\\s?\\w{2}$', 'Invalid zip code.')])),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('lat', models.CharField(blank=True, max_length=20, null=True)),
                ('lon', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quarter', models.CharField(max_length=8)),
                ('year', models.PositiveSmallIntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('is_return', models.BooleanField(default=True)),
                ('distance', models.PositiveSmallIntegerField(default=0)),
                ('allowance', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('api_return_code', models.CharField(blank=True, max_length=3, null=True)),
                ('api_message', models.CharField(blank=True, max_length=500, null=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='trip_to', to='kilometers.Location')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='trip_from', to='kilometers.Location')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
