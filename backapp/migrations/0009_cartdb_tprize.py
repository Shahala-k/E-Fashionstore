# Generated by Django 4.1.3 on 2023-02-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0008_remove_cartdb_category_remove_cartdb_pdctname'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='TPRIZE',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
