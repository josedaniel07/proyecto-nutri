# Generated by Django 3.2.7 on 2021-09-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210911_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='estado',
            field=models.CharField(default='No Pagado', max_length=10),
        ),
    ]
