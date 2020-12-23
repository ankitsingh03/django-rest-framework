# Generated by Django 2.1.5 on 2020-12-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batting_team', models.CharField(max_length=50)),
                ('batsman', models.CharField(max_length=50)),
                ('batsman_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
            ],
        ),
    ]
