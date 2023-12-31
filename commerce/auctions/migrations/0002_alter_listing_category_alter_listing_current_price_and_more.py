# Generated by Django 4.2.3 on 2023-08-09 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='current_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
