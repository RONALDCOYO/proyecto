from django.contrib import admin
from .models import Cliente, Proveedor, Producto, Venta

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)
