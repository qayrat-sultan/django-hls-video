# Generated by Django 2.2.2 on 2019-06-28 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_auto_20190625_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='public',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False),
        ),
    ]
