# Generated by Django 5.0.6 on 2024-07-25 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0003_examcenter2_myexamcenter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myexamcenter',
            options={'ordering': ['-id']},
        ),
    ]
