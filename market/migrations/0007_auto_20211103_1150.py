# Generated by Django 3.2.8 on 2021-11-03 11:50

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20211026_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='crop',
            field=image_cropping.fields.ImageRatioField('image', '100x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='crop'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=image_cropping.fields.ImageCropField(upload_to='product'),
        ),
    ]