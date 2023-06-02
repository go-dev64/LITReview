# Generated by Django 4.2.1 on 2023-06-02 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("follower", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfollows",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follow",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
