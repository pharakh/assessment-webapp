# Generated by Django 4.1.1 on 2022-09-26 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0017_alter_course_options_alter_teacher_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor_of_TA', to='assessment_app.teacher'),
        ),
    ]