# Generated by Django 4.1 on 2023-08-14 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Book", "0003_rename_page_num_bookfile_page"),
        ("Comment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentinfo",
            name="file_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Book.bookfile",
            ),
        ),
    ]
