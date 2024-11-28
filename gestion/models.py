from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.utils import timezone
from datetime import timedelta



class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='logos_empresas/', null=True, blank=True)  # Campo para la imagen del logo

    def __str__(self):
        return self.nombre
    
from django.db import models


class Dependencia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    inicio_consecutivo = models.IntegerField(default=1)  # Agrega este campo

    def __str__(self):
        return f"{self.nombre} - {self.empresa.nombre}"

    

class gestion_empresa(models.Model):
    nombre = models.CharField(max_length=100)  # Campo para el nombre de la empresa

    def __str__(self):
        return self.nombre  # Esto permitirá que el nombre de la empresa se muestre en el formulario

    
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresas = models.ManyToManyField(Empresa, blank=True)  # Ahora un usuario puede estar en varias empresas
    dependencias = models.ManyToManyField(Dependencia, blank=True)

    def __str__(self):
        return f"{self.user.username} - {', '.join([empresa.nombre for empresa in self.empresas.all()])}"


class Correspondencia(models.Model):
    TIPO_CORRESPONDENCIA = [
        ('Carta', 'Carta'),
        ('Memorando', 'Memorando'),
        ('Email', 'Email'),
        ('DP', 'DP'),
    ]

    ENTRADA_SALIDA = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    ]

    entrada_salida = models.CharField(max_length=10, choices=ENTRADA_SALIDA)
    tipo_correspondencia = models.CharField(max_length=20, choices=TIPO_CORRESPONDENCIA)
    consecutivo = models.CharField(max_length=100, blank=True, null=True)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    documento = models.FileField(upload_to='correspondencias/', null=True, blank=True)
    asunto = models.CharField(max_length=255)
    remitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    necesita_respuesta = models.BooleanField(default=False)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    fecha_limite_respuesta = models.DateTimeField(null=True, blank=True) 
    respondida = models.BooleanField(default=False)
    respuesta = models.TextField(blank=True, null=True)
    documento_respuesta = models.FileField(upload_to='respuestas/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Convertir los campos de texto a mayúsculas
        if self.asunto:
            self.asunto = self.asunto.upper()
        if self.remitente:
            self.remitente = self.remitente.upper()
        if self.destinatario:
            self.destinatario = self.destinatario.upper()

        # Generar el consecutivo si es una nueva instancia
        if not self.pk:
            print(f"Inicio consecutivo de la dependencia '{self.dependencia.nombre}': {self.dependencia.inicio_consecutivo}")

            # Obtener el último consecutivo de la dependencia
            ultima_correspondencia = Correspondencia.objects.filter(
                dependencia=self.dependencia
            ).order_by('-id').first()

            if ultima_correspondencia:
                ultimo_numero = int(ultima_correspondencia.consecutivo.split('-')[-1])
                nuevo_consecutivo = ultimo_numero + 1
                print(f"Último consecutivo encontrado: {ultimo_numero}")
            else:
                nuevo_consecutivo = self.dependencia.inicio_consecutivo
                print(f"No se encontraron correspondencias previas. Usando inicio_consecutivo: {nuevo_consecutivo}")

            self.consecutivo = f"{self.dependencia.empresa.codigo}-{self.dependencia.codigo}-{timezone.now().year}-{nuevo_consecutivo:02d}"
            print(f"Nuevo consecutivo generado: {self.consecutivo}")

        # Llamar al método save original
        super(Correspondencia, self).save(*args, **kwargs)

    def calcular_fecha_limite_respuesta(self, dias_para_responder):
        self.fecha_limite_respuesta = self.fecha + timedelta(days=dias_para_responder)
        self.save()
    
    def marcar_como_respondida(self, respuesta_texto):
        self.respondida = True
        self.respuesta = respuesta_texto
        self.fecha_respuesta = timezone.now()
        self.save()

    def __str__(self):
        return f"GRD-{self.dependencia.codigo}-{timezone.now().year}-{self.consecutivo}"

    



class RespuestaCorrespondencia(models.Model):
    correspondencia = models.ForeignKey(Correspondencia, on_delete=models.CASCADE)
    respuesta = models.TextField()
    fecha_respuesta = models.DateField()
    documento_respuesta = models.FileField(upload_to='respuestas/', null=True, blank=True)  # Nuevo campo para el documento
