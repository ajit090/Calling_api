# Generated by Django 3.2.7 on 2022-01-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company_type',
            field=models.CharField(choices=[('company', 'company'), ('end customer', 'end customer')], default='company', max_length=20),
        ),
    ]
