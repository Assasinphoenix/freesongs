# Generated by Django 2.1.7 on 2019-03-16 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('C', 'Classic'), ('S', 'Sad'), ('H', 'Happy'), ('M', 'Melody'), ('D', 'Devotional')], max_length=1)),
                ('song', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('year', models.IntegerField()),
                ('director', models.CharField(blank=True, max_length=100)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('C', 'Classic'), ('S', 'Sad'), ('H', 'Happy'), ('M', 'Melody'), ('D', 'Devotional')], max_length=1)),
                ('song', models.FileField(blank=True, upload_to='')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='audio',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Movie'),
        ),
    ]