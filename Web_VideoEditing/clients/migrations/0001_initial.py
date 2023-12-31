# Generated by Django 4.2.8 on 2023-12-21 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_users_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to='audio_files/')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_video', models.FileField(upload_to='Files/')),
                ('title_video', models.CharField(max_length=200)),
                ('path_image', models.FileField(upload_to='Files/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('video_edit', models.FileField(upload_to='video_edits/')),
                ('duration', models.IntegerField()),
                ('format', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('update_date', models.DateTimeField()),
                ('thumb', models.ImageField(upload_to='video_thumbs/')),
                ('subtitle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.subtitle')),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.upload')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='UserUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.upload')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
