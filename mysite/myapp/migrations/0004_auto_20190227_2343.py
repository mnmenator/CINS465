# Generated by Django 2.1.7 on 2019-02-27 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_suggestion_suggestion_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suggestion',
            new_name='ToDo',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='suggestion_field',
            new_name='todo_field',
        ),
    ]
