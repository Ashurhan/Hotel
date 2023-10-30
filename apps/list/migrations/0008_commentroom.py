# Generated by Django 4.2.6 on 2023-10-27 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0007_delete_blog_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_commnets', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sybcommnets', to='list.commentroom')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='list.rooms')),
            ],
        ),
    ]