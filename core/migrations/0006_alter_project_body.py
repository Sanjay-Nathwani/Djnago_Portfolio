# Generated by Django 4.2.1 on 2023-05-22 19:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_project_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="body",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
