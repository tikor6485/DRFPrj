# Generated by Django 3.2.5 on 2021-07-19 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='new_Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='new_Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='new_Name',
            new_name='name',
        ),
    ]
