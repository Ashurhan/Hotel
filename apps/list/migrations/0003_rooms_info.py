# Generated by Django 4.2.6 on 2023-10-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_remove_rooms_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='info',
            field=models.CharField(max_length=500, null=True, verbose_name='описание'),
        ),
    ]