# Generated by Django 4.1.2 on 2022-11-23 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='purcase_date',
            new_name='purchase_date',
        ),
    ]
