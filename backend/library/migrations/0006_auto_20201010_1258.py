# Generated by Django 3.1.2 on 2020-10-10 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201006_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='affiliation',
            new_name='group',
        ),
    ]
