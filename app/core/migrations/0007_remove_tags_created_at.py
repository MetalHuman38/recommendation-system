# Generated by Django 4.2.16 on 2024-10-20 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_tags_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='created_at',
        ),
    ]
