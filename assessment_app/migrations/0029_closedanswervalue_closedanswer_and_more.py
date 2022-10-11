# Generated by Django 4.1.1 on 2022-09-27 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0028_rename_form_course_form_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedAnswerValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClosedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_radio', models.PositiveSmallIntegerField()),
                ('values', models.ManyToManyField(related_name='enrolled_students', to='assessment_app.closedanswervalue')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='a_closed_vals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_ans_vals', to='assessment_app.closedanswer'),
        ),
    ]
