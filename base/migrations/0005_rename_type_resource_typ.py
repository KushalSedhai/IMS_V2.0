# Generated by Django 5.0.6 on 2024-05-12 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_vendor_resource_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='type',
            new_name='typ',
        ),
    ]