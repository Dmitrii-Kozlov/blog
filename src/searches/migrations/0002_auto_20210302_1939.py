# Generated by Django 3.1.7 on 2021-03-02 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchquery',
            old_name='qurey',
            new_name='query',
        ),
    ]
