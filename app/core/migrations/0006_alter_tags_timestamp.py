# Generated by Django 4.2.16 on 2024-10-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_tags_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]