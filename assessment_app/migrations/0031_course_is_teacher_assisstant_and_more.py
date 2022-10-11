# Generated by Django 4.1.1 on 2022-09-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0030_rename_a_closed_vals_questions_answer_closed_vals'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_teacher_assisstant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='closedanswer',
            name='values',
            field=models.ManyToManyField(related_name='answer_values', to='assessment_app.closedanswervalue'),
        ),
    ]
