# Generated by Django 5.1.1 on 2024-09-27 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_created_on_task_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
