# Generated by Django 4.0.5 on 2022-06-30 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quastion',
            old_name='acked',
            new_name='asked',
        ),
    ]
