# Generated by Django 4.1.5 on 2023-02-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0007_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='backlog',
            field=models.IntegerField(),
        ),
    ]