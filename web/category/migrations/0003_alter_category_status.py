# Generated by Django 4.1.4 on 2023-02-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0),
        ),
    ]
