# Generated by Django 3.2.7 on 2021-10-10 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_menu_lista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='lista',
        ),
    ]