# Generated by Django 4.1.1 on 2022-10-03 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0043_alter_teacher_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='assessment_app/static/assessment_app/img'),
        ),
    ]
