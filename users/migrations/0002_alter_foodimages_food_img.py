# Generated by Django 3.2.3 on 2021-05-15 14:22

from django.db import migrations, models
import foodfinds.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodimages',
            name='food_img',
            field=models.FileField(storage=foodfinds.storage_backends.MediaStorage(), upload_to='foods/'),
        ),
    ]
