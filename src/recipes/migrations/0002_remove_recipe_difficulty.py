# Generated by Django 5.0.6 on 2024-05-22 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="difficulty",
        ),
    ]
