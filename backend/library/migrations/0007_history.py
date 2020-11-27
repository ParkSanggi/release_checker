# Generated by Django 3.1.2 on 2020-10-28 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20201010_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='library.library')),
            ],
        ),
    ]