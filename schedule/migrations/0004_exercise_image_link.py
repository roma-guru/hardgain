# Generated by Django 2.0 on 2018-01-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20180102_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image_link',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
