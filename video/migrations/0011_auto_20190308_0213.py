# Generated by Django 2.0.6 on 2019-03-08 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_auto_20190308_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocollection',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
