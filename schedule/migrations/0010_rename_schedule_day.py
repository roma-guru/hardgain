from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('schedule', '0009_auto_20180403_1351'),
    ]

    operations = [
        migrations.RenameModel(
            'ScheduleDay', 'DayProgram'
        ),
    ]
