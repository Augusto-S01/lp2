# Generated by Django 5.1.3 on 2024-12-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='professional_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
