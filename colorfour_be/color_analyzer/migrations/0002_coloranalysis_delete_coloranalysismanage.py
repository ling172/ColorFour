# Generated by Django 4.2 on 2024-08-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('color_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('season', models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn'), ('Winter', 'Winter')], max_length=6)),
                ('skin_color', models.CharField(max_length=50)),
                ('hair_color', models.CharField(max_length=50)),
                ('eye_color', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('test_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ColorAnalysisManage',
        ),
    ]