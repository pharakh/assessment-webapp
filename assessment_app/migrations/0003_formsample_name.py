# Generated by Django 4.1.1 on 2022-09-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0002_rename_q_ans_c_queandans_q_ans_closed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsample',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
