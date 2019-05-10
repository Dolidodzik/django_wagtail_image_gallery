# Generated by Django 2.2.1 on 2019-05-10 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('gallery', '0005_miniature'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerysubpage',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.DeleteModel(
            name='Miniature',
        ),
    ]
