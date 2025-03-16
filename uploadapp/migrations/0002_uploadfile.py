# Generated by Django 5.1.6 on 2025-03-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='files')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
