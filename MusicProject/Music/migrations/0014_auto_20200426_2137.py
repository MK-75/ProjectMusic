# Generated by Django 3.0.3 on 2020-04-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0013_merge_20200426_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
