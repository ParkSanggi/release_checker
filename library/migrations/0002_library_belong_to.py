# Generated by Django 3.1.2 on 2020-10-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='belong_to',
            field=models.CharField(default='maven', max_length=20),
        ),
    ]
