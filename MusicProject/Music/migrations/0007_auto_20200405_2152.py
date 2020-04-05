# Generated by Django 3.0.3 on 2020-04-05 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0006_auto_20200405_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='images/songs')),
                ('album_name', models.CharField(max_length=100)),
                ('total_tracks', models.IntegerField()),
                ('genre', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Music.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Music.Album'),
        ),
    ]
