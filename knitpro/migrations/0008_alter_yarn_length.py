# Generated by Django 4.2.1 on 2023-05-29 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knitpro', '0007_alter_yarn_brand_alter_yarn_length_alter_yarn_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarn',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
