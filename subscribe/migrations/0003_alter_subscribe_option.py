# Generated by Django 5.1.6 on 2025-03-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_subscribe_option_alter_subscribe_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'WEEKLY'), ('M', 'MONTHLY')], default='M', max_length=2),
        ),
    ]
