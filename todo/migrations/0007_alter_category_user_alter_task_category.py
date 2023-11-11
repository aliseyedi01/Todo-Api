# Generated by Django 4.2.7 on 2023-11-10 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0006_alter_category_user_alter_task_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.category'),
        ),
    ]