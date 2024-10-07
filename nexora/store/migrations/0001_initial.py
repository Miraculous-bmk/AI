# Generated by Django 5.0.6 on 2024-10-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('channels', models.JSONField()),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
