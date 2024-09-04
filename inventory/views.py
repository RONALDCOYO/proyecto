from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Proveedor, Producto, Venta
from .forms import ClienteForm, ProveedorForm, VentaForm
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import ClienteSerializer, ProductoSerializer, VentaSerializer

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventory/product_list.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventory/product_detail.html', {'producto': producto})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'inventory/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'inventory/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'inventory/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'inventory/cliente_confirm_delete.html', {'cliente': cliente})

def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventory/proveedor_list.html', {'proveedores': proveedores})

def proveedor_create(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'inventory/proveedor_form.html', {'form': form})

def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'inventory/proveedor_form.html', {'form': form})

def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        proveedor.delete()
        return redirect('proveedor_list')
    return render(request, 'inventory/proveedor_confirm_delete.html', {'proveedor': proveedor})
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'inventory/venta_list.html', {'ventas': ventas})

def venta_create(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'inventory/venta_form.html', {'form': form})

def venta_update(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'inventory/venta_form.html', {'form': form})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        venta.delete()
        return redirect('venta_list')
    return render(request, 'inventory/venta_confirm_delete.html', {'venta': venta})


# Similar para clientes, proveedores y ventas

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes_list.html'  # Nombre de la plantilla para mostrar la lista
    context_object_name = 'clientes'      # El nombre del contexto que se usará en la plantilla

    def get_queryset(self):
        return Cliente.objects.all()  # Retorna todos los clientes, puedes modificar este queryset si es necesario


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

