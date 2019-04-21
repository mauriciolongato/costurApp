from django.contrib import admin
from core.models.objects \
    import Cliente, Pedido, Referencia, PedidoSKU, Funcionario, Pistola, Maquina, \
    Sequencia, Alocacao, BackLog, LogTrabalho, Acao, SequenciaAcao, Caixa


# Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cliente._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Cliente._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


# Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Pedido._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Pedido._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


# Referencia
class ReferenciaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Referencia._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Referencia._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


# Pedido_SKU
class PedidoSKUAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PedidoSKU._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in PedidoSKU._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


# Funcionario
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Funcionario._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Funcionario._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


# Pistola
class PistolaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Pistola._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Pistola._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


# Maquina
class MaquinaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Maquina._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Maquina._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


# Caixa
class CaixaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Caixa._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Caixa._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


# Acao
class AcaoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Acao._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Acao._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


# Sequencia
class SequenciaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Sequencia._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Sequencia._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


class SequenciaAcaoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SequenciaAcao._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in SequenciaAcao._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


# Alocacao
class AlocacaoAdmin(admin.ModelAdmin):
    fields = ('referencia', 'pedido', 'sequencia', 'capacidade_caixa')
    list_display = [f.name for f in Alocacao._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Alocacao._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


# BackLog
class BackLogAdmin(admin.ModelAdmin):
    list_display = [f.name for f in BackLog._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in BackLog._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


# Log_Traballho
class LogTrabalhoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in LogTrabalho._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in LogTrabalho._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 10


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Referencia, ReferenciaAdmin)
admin.site.register(PedidoSKU, PedidoSKUAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Pistola, PistolaAdmin)
admin.site.register(Maquina, MaquinaAdmin)
admin.site.register(Sequencia, SequenciaAdmin)
admin.site.register(SequenciaAcao, SequenciaAcaoAdmin)
admin.site.register(Acao, AcaoAdmin)
admin.site.register(Alocacao, AlocacaoAdmin)
admin.site.register(BackLog, BackLogAdmin)
admin.site.register(LogTrabalho, LogTrabalhoAdmin)
admin.site.register(Caixa, CaixaAdmin)
