# Generated by Django 4.1.3 on 2022-12-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]