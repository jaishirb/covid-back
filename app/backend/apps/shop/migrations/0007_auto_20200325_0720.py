# Generated by Django 2.2 on 2020-03-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidoindividual',
            name='color',
            field=models.CharField(max_length=8),
        ),
    ]