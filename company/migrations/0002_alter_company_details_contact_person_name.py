# Generated by Django 3.2.7 on 2021-12-31 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='Contact_person_Name',
            field=models.CharField(max_length=100),
        ),
    ]