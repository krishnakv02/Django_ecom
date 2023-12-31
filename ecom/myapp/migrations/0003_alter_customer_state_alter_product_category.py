# Generated by Django 4.2 on 2023-04-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_customer_state_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('karnataka', 'karnataka'), ('kerala', 'kerala'), ('tamilnadu', 'tamilnadu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('sb', 'SKETCH BOOK'), ('wr', 'WATERCOLOUR'), ('dp', 'DRAWING PAPER'), ('gp', 'GRAPHITE PENCIL'), ('ar', 'ACRYLIC')], max_length=200),
        ),
    ]
