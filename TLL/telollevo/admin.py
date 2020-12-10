from django.contrib import admin

# Register your models here.

from . models import UsuarioEmpresa, UsuarioRepartidor, Vehiculo, Envios

class UsusarioEmpresaAdmin(admin.ModelAdmin):
	list_display=("nombreEmpresa", "rutEmpresa", "direccionEmpresa", "correoEmpresa", "telefonoEmpresa")

class UsusarioRepartidorAdmin(admin.ModelAdmin):
	list_display=("rutRepartidor", "apellidosRepartidor", "nombreRepartidor",  "telefonoRepartidor", "correoRepartidor")

class VehiculoAdmin(admin.ModelAdmin):
	list_display=("patente", "usuarioR", "marca",  "modelo", "año")

class EnviosAdmin(admin.ModelAdmin):
	list_display=("id", "direccionDestino", "nombreDestino",  "rutDestino", "telefonoDestino", "correoDestino", "estadoEnvio")


admin.site.register(UsuarioEmpresa, UsusarioEmpresaAdmin)
admin.site.register(UsuarioRepartidor, UsusarioRepartidorAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Envios, EnviosAdmin)