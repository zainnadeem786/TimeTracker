# Generated by Django 5.1.2 on 2024-10-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worksession',
            old_name='screenshots',
            new_name='screenshot_paths',
        ),
        migrations.AlterField(
            model_name='worksession',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
