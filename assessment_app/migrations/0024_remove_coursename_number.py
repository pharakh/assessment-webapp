# Generated by Django 4.1.1 on 2022-09-27 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0023_alter_coursename_number_alter_coursename_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursename',
            name='number',
        ),
    ]