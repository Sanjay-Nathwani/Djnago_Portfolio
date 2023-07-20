# Generated by Django 4.2.1 on 2023-05-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_message"),
    ]

    operations = [
        migrations.CreateModel(
            name="Endorsement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("body", models.TextField()),
                ("featured", models.BooleanField(default=True)),
            ],
        ),
    ]
