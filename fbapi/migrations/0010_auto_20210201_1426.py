# Generated by Django 3.1.4 on 2021-02-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbapi', '0009_comments_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='source',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram')], default='Facebook', max_length=1000, null=True),
        ),
    ]
