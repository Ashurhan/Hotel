# Generated by Django 4.2.6 on 2023-10-09 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='назвние')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000, null=True)),
                ('phone', models.CharField(max_length=14, verbose_name='номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=120, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('size', models.SmallIntegerField(null=True, verbose_name='размер')),
                ('services', models.CharField(max_length=100, null=True, verbose_name='сервисы')),
                ('bed', models.CharField(max_length=120, null=True, verbose_name='кровать')),
                ('is_available', models.BooleanField(default=True)),
                ('persons', models.CharField(max_length=20, null=True, verbose_name='persons')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='list.category')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.CreateModel(
            name='RoomIMage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='media')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='list.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(null=True, verbose_name='Дата заезда')),
                ('check_out', models.DateField(null=True, verbose_name='Дата выезда')),
                ('adult', models.PositiveSmallIntegerField(default=1, null=True, verbose_name='Adult')),
                ('children', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Children')),
                ('sum', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='list.contact')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='list.rooms')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
