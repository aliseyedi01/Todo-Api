# Generated by Django 4.2.7 on 2023-11-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_category_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_by',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]