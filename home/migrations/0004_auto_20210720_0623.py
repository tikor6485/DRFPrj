# Generated by Django 3.2.5 on 2021-07-20 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210719_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='ageee',
            new_name='newAge',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='eeemail',
            new_name='newEmail',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='nameee',
            new_name='newName',
        ),
    ]
