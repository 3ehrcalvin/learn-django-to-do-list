# Generated by Django 5.1.5 on 2025-02-05 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_list_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
