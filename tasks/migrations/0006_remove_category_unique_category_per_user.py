# Generated by Django 4.2.7 on 2023-11-12 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_category_unique_category_per_user'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='category',
            name='unique_category_per_user',
        ),
    ]
