# Generated by Django 2.1.3 on 2018-11-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('date1', models.BooleanField(default=False)),
                ('date2', models.BooleanField(default=False)),
                ('date1_confirmed', models.DateField(blank=True)),
                ('date2_confirmed', models.DateField(blank=True)),
            ],
        ),
    ]
