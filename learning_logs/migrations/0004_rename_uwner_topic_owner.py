# Generated by Django 5.1.2 on 2024-11-04 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_uwner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='uwner',
            new_name='owner',
        ),
    ]
