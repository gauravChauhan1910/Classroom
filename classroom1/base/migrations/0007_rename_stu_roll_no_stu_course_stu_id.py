# Generated by Django 4.0.4 on 2022-06-06 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_prof_course_prof_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stu_course',
            old_name='stu_roll_no',
            new_name='stu_id',
        ),
    ]