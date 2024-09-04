from django.urls import path
from rest_framework import routers
from . import views
from .views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView,
    VentaListView, VentaCreateView, VentaUpdateView, VentaDeleteView, ProductoListView, ProductoDetailView,
    ProductoCreateView, ProductoUpdateView, ProductoDeleteView
)


router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'ventas', views.VentaViewSet)

urlpatterns = [
        
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detalle'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto-nuevo'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto-editar'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto-eliminar'),
    
    
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
