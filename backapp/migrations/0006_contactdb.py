# Generated by Django 4.1.3 on 2023-02-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0005_alter_productdb_prize'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL', models.EmailField(blank=True, max_length=100, null=True)),
                ('MESSAGE', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]