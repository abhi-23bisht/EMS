# Generated by Django 5.0.7 on 2024-07-20 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0004_rename_mob_employee_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='id',
            new_name='emp_id',
        ),
    ]
