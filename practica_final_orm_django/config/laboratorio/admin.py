from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto

# Register your models here.
@admin.register(DirectorGeneral)
# Personalizo la vista del panel para ver el listado de registros con los atributos.
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Producto)
# Personalizo la vista del panel para ver el listado de registros con los atributos.
# Además agrego un filtro por nombre y por laboratorio para los productos.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('nombre', 'laboratorio')