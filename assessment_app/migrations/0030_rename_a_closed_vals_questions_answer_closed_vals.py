# Generated by Django 4.1.1 on 2022-09-27 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0029_closedanswervalue_closedanswer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='a_closed_vals',
            new_name='answer_closed_vals',
        ),
    ]
