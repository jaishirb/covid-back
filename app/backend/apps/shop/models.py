from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models

from backend.apps.utils.constants import SHOP_STATUS
from backend.apps.utils.models import ModelBase


class Categoria(ModelBase):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Color(ModelBase):
    nombre = models.CharField(max_length=45)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'


class Producto(ModelBase):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(
        blank=True,
        null=True
    )
    imagen = models.FileField(upload_to='images')
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    colores = models.ManyToManyField(Color)

    def __str__(self):
        return self.nombre + '/' + self.categoria.nombre

    def get_precio(self):
        return intcomma(self.precio)

    def save(self, *args, **kwargs):
        flag = self.pk is None
        super(Producto, self).save(*args, **kwargs)
        if flag:
            Inventario.objects.create(producto=self)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class PedidoIndividual(ModelBase):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    color = models.CharField(max_length=12)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return str(self.producto) + " " + self.color + " x" + str(self.cantidad)

    class Meta:
        verbose_name = 'Pedido individual'
        verbose_name_plural = 'Pedidos individuales'


class Pedido(ModelBase):
    pedidos_individuales = models.ManyToManyField(PedidoIndividual)
    domicilio_cliente = models.CharField(max_length=120)
    telefono_cliente = models.CharField(max_length=12)
    nombre_cliente = models.CharField(max_length=45)
    total = models.FloatField(
        blank=True,
        null=True
    )
    estado = models.CharField(
        max_length=45,
        choices=SHOP_STATUS,
        default='pendiente'
    )
    fecha_entrega = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id) + " " + str(self.estado)

    def save(self, *args, **kwargs):
        super(Pedido, self).save(*args, **kwargs)
        total = 0
        for pedido in self.pedidos_individuales.all():
            total += pedido.producto.precio*pedido.cantidad
        self.total = total
        super(Pedido, self).save(update_fields=['total'])

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class Inventario(ModelBase):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    ultima_modificacion = models.DateField(auto_now=True)
    vendidos = models.PositiveIntegerField(default=0)
    total_ventas = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.total_ventas = self.vendidos*self.producto.precio
        super(Inventario, self).save(*args, **kwargs)

    def __str__(self):
        return self.producto.nombre + " " + str(self.stock)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Inventario'
