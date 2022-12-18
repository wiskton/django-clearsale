# -*- coding: utf-8 -*-
from django.contrib import admin
from models import PedidoItem, Pedido, Entrega, Cobranca


class PedidoItemInline( admin.TabularInline ):
    model = PedidoItem
    readonly_fields = ['item_id', 'item_nome', 'item_qtd', 'item_valor', 'item_categoria', ]
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido_id', 'data', 'ip', 'risco', 'status',)
    search_fields = ('pedido_id', 'data', 'ip', 'status',)
    list_filter = ['status',]
    list_editable = ['status',]
    readonly_fields = ['pedido_id', 'data', 'ip', 'total', 'tipo_pagamento', 'tipo_cartao', 'parcelas',]
    inlines = [PedidoItemInline,]
    save_on_top = True
    list_per_page = 20

admin.site.register(Pedido,PedidoAdmin)

# class PedidoItemAdmin(admin.ModelAdmin):
#     # list_display = ('nome',)
#     # search_fields = ('nome',)
#     #list_filter = ['ativo',]
#     #list_editable = ['ativo']
#     #readonly_fields = ['cliques',]
#     save_on_top = True
#     list_per_page = 20

# admin.site.register(PedidoItem,PedidoItemAdmin)

# class CobrancaAdmin(admin.ModelAdmin):
#     # list_display = ('nome',)
#     # search_fields = ('nome',)
#     #list_filter = ['ativo',]
#     #list_editable = ['ativo']
#     #readonly_fields = ['cliques',]
#     save_on_top = True
#     list_per_page = 20

# admin.site.register(Cobranca,CobrancaAdmin)

# class EntregaAdmin(admin.ModelAdmin):
#     # list_display = ('nome',)
#     # search_fields = ('nome',)
#     #list_filter = ['ativo',]
#     #list_editable = ['ativo']
#     #readonly_fields = ['cliques',]
#     save_on_top = True
#     list_per_page = 20

# admin.site.register(Entrega,EntregaAdmin)
