# Generated by Django 4.2.9 on 2024-02-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={
                "get_latest_by": "date_started",
                "ordering": ["date_started"],
                "verbose_name_plural": "Tasks",
            },
        ),
        migrations.AlterUniqueTogether(
            name="task",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="task",
            name="date_started",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
