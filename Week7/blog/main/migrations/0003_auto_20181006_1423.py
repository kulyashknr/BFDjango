# Generated by Django 2.1.1 on 2018-10-06 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created',
        ),
    ]