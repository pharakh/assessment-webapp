# Generated by Django 4.1.1 on 2022-09-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0035_prizename_prizesgot_delete_prize'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]