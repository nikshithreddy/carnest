# Generated by Django 5.1.4 on 2024-12-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingride',
            name='chat',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]