# Generated by Django 2.1.5 on 2020-12-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_deliveries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('team1', models.CharField(max_length=50)),
                ('team2', models.CharField(max_length=50)),
            ],
        ),
    ]
