from django.urls import path
from rest_framework import routers
from . import views
from .views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView,
    VentaListView, VentaCreateView, VentaUpdateView, VentaDeleteView
)


router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'ventas', views.VentaViewSet)

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    # Similar para clientes, proveedores y ventas
     # URLs para Cliente
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # URLs para Proveedor
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedores/editar/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedores/eliminar/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_delete'),

    # URLs para Venta
    path('ventas/', VentaListView.as_view(), name='venta_list'),
    path('ventas/nuevo/', VentaCreateView.as_view(), name='venta_create'),
    path('ventas/editar/<int:pk>/', VentaUpdateView.as_view(), name='venta_update'),
    path('ventas/eliminar/<int:pk>/', VentaDeleteView.as_view(), name='venta_delete'),

]
