# Generated by Django 2.0 on 2018-01-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20180102_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycle',
            name='type',
        ),
        migrations.AddField(
            model_name='cycle',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
