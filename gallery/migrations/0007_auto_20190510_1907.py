# Generated by Django 2.2.1 on 2019-05-10 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20190510_0518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallerysubpage',
            old_name='cover',
            new_name='miniature',
        ),
    ]
