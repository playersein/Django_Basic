# Generated by Django 4.2.4 on 2023-09-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(),
        ),
    ]