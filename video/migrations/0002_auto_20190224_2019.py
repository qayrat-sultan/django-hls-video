# Generated by Django 2.0.6 on 2019-02-24 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videofile',
            name='raw_video_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
