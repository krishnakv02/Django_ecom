# Generated by Django 4.2 on 2023-04-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('kerala', 'kerala'), ('karnataka', 'karnataka'), ('tamilnadu', 'tamilnadu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('sb', 'SKETCH BOOK'), ('dp', 'DRAWING PAPER'), ('ar', 'ACRYLIC'), ('gp', 'GRAPHITE PENCIL'), ('wr', 'WATERCOLOUR')], max_length=200),
        ),
    ]