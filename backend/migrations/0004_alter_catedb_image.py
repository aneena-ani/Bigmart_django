# Generated by Django 5.0.4 on 2024-05-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_catedb_description_alter_prodb_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category image'),
        ),
    ]
