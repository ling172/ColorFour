# Generated by Django 4.2 on 2024-10-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothsubcategory',
            name='temperature',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]