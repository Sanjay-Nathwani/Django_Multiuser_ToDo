# Generated by Django 4.2.1 on 2023-07-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="status",
            field=models.CharField(
                choices=[("C", "Completed"), ("P", "Pending")], max_length=2
            ),
        ),
    ]
