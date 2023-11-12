# Generated by Django 4.2.7 on 2023-11-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_category_per_user'),
        ),
    ]
