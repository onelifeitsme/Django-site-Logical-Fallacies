# Generated by Django 3.2.6 on 2021-09-15 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallacies', '0002_alter_fallacy_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fallacy',
            name='example',
        ),
        migrations.AddField(
            model_name='fallacy',
            name='example1_image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='fallacy',
            name='example1_text',
            field=models.TextField(default='Пример 1'),
        ),
        migrations.AddField(
            model_name='fallacy',
            name='example2_image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='fallacy',
            name='example2_text',
            field=models.TextField(default='Пример 2'),
        ),
    ]
