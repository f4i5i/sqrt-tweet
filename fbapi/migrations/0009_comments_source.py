# Generated by Django 3.1.4 on 2021-02-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapi', '0008_page_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='source',
            field=models.CharField(default='Facebook', max_length=1000, null=True),
        ),
    ]
