# Generated by Django 4.2.7 on 2023-11-20 10:53

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
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('user1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversations_user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversations_user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]