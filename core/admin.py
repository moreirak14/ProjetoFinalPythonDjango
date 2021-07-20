from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametros, MovRotativo, Mensalista

# Register your models here.

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'veiculo','valor_hora', 'horas_total','total', 'pago')

admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovRotativo, MovRotativoAdmin)