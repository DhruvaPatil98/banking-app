# Generated by Django 3.0.3 on 2020-02-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_transactions_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='action',
            field=models.CharField(max_length=7),
        ),
    ]
