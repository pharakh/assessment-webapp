# Generated by Django 4.1.1 on 2022-09-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0020_remove_teacher_supervisor_teacher_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursename',
            name='number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursename',
            name='type',
            field=models.CharField(default='', max_length=10),
        ),
    ]
