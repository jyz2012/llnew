# Generated by Django 5.1 on 2024-08-24 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='public',
        ),
    ]
