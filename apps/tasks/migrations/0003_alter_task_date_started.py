# Generated by Django 4.2.9 on 2024-02-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_task_options_alter_task_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="date_started",
            field=models.DateTimeField(),
        ),
    ]
