# Generated by Django 4.1.3 on 2023-01-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('DISCRIPTION', models.CharField(blank=True, max_length=100, null=True)),
                ('IMAGE', models.ImageField(upload_to='profile')),
            ],
        ),
    ]
