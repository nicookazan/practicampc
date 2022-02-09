from django.contrib import admin

# Register your models here.
from computadoras.models import *
admin.site.register(Monitor)
admin.site.register(Computadora)
admin.site.register(Teclado)
admin.site.register(Mouse)