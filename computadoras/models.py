from django.db import models

# Create your models here.

class Monitor(models.Model):
    nombre = models.CharField(max_length=255, default='')
    marca = models.CharField(max_length=255)
    width = models.IntegerField()
    def __str__(self):
        return f'Monitor {self.id}: {self.nombre} {self.marca} {self.width}'

class Teclado(models.Model):
    nombre = models.CharField(max_length=255, default='')
    marca = models.CharField(max_length=255)
    tipo_entrada = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    def __str__(self):
        return f'Teclado {self.id}: {self.nombre} {self.marca} {self.tipo_entrada} {self.tipo}'


class Mouse(models.Model):
    nombre = models.CharField(max_length=255, default='')
    marca = models.CharField(max_length=255)
    tipo_entrada = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    def __str__(self):
        return f'Mouse {self.id}: {self.nombre} {self.marca} {self.tipo_entrada} {self.tipo}'

class Computadora(models.Model):
    nombre = models.CharField(max_length=255)
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True)
    teclado = models.ForeignKey(Teclado, on_delete=models.SET_NULL, null=True)
    mouse = models.ForeignKey(Mouse, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'PC {self.id}: {self.nombre} Monitor: {self.monitor.nombre} Teclado: {self.teclado.nombre} Mouse: {self.mouse.nombre}'