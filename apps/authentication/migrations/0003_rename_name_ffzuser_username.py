# Generated by Django 3.2.6 on 2021-12-27 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20211227_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ffzuser',
            old_name='name',
            new_name='username',
        ),
    ]