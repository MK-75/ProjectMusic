# Generated by Django 3.0.3 on 2020-04-29 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0016_auto_20200427_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='song',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Music.Song'),
        ),
    ]
