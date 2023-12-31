# Generated by Django 4.2.6 on 2023-11-08 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0010_alter_commentroom_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('phone', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=100)),
                ('time', models.DateTimeField(null=True, verbose_name='Время брони')),
                ('persons', models.PositiveSmallIntegerField(default=1, null=True, verbose_name='Persons')),
                ('message', models.TextField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='RestaurantMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('info', models.TextField(verbose_name='Описание')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='m_category', to='list.category')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurantimage', models.ImageField(upload_to='media/')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to='list.restaurantmenu')),
            ],
        ),
    ]
