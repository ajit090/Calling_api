# Generated by Django 3.2.7 on 2021-12-31 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=100)),
                ('Contact_person_Name', models.EmailField(max_length=100)),
                ('Email', models.EmailField(max_length=200)),
                ('Contact_1', models.CharField(max_length=100)),
                ('Contact_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
    ]
