# Generated by Django 3.2.22 on 2023-11-25 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_complaint_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='Engine_number',
            new_name='Chasis_number',
        ),
    ]