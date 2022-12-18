# -*- coding: utf-8 -*-
from django.db import models

class Pedido(models.Model):

    STATUS_CHOICE = (
        ('PEN', 'Pendente'),
        ('CAN', 'Cancelado pelo cliente'),
        ('SUS', 'Suspeito'),
        ('APM', 'Aprovado'),
        ('FRD', 'Fraude Confirmada'),
        ('RPM', 'Reprovado'),
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    pedido_id = models.CharField(u'Código do pedido', max_length=50)
    data = models.CharField(u'Data do pedido', max_length=19)
    total = models.FloatField(u'Valor total do pedido', max_length=9)
    tipo_pagamento = models.IntegerField(u'Tipo de Pagamento do Pedido (Lista de Valores)', max_length=2)
    parcelas = models.IntegerField(u'Número de Parcelas', max_length=2)
    # não obrigatórios
    tipo_cartao = models.IntegerField(u'Bandeira do Cartão (Lista de Valores)', max_length=2, null=True, blank=True)
    ip = models.CharField(u'IP do Pedido', max_length=25, null=True, blank=True)
    # campo que irá salvar o retorno
    risco = models.CharField(u'Risco', max_length=255)
    status = models.CharField(u'Status', max_length=10, default='PEN', choices=STATUS_CHOICE)

    def __unicode__(self):
        return self.pedido_id


class PedidoItem(models.Model):

    class Meta:
        ordering = ('-item_id',)
        verbose_name = 'Item'
        verbose_name_plural = 'Itens do Pedido'

    pedido = models.ForeignKey(Pedido)
    item_id = models.CharField(u'Código', max_length=50)
    item_nome = models.CharField(u'Nome', max_length=150)
    item_qtd = models.IntegerField(u'Quantidade', max_length=2)
    item_valor = models.FloatField(u'Valor', max_length=9)
    # não obrigatórios
    item_categoria = models.CharField(u'Nome da Categoria', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.item_id

class Cobranca(models.Model):

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Cobrança'
        verbose_name_plural = 'Cobranças'

    nome = models.CharField(u'Nome', max_length=500)
    email = models.CharField(u'Email', max_length=150)
    documento = models.CharField(u'CPF ou CNPJ', max_length=100)
    endereco = models.CharField(u'Endereço', max_length=200)
    numero = models.CharField(u'Número do Texto Endereço', max_length=15)
    complemente = models.CharField(u'Complemento', max_length=250)
    bairro = models.CharField(u'Bairro', max_length=150)
    cidade = models.CharField(u'Cidade', max_length=150)
    estado = models.CharField(u'Estado', max_length=2)
    cep = models.CharField(u'CEP', max_length=10)
    pais = models.CharField(u'País', max_length=3)
    ddd_telefone = models.CharField(u'Código de Àrea', max_length=2)
    telefone = models.CharField(u'Número de Telefone', max_length=8)
    # não obrigatórios
    ddd_celular = models.CharField(u'Código de Àrea', max_length=2, null=True, blank=True)
    celular = models.CharField(u'Número do Celular', max_length=8, null=True, blank=True)

    def __unicode__(self):
        return self.nome

class Entrega(models.Model):

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'

    nome = models.CharField(u'Nome', max_length=500)
    email = models.CharField(u'Email', max_length=150)
    documento = models.CharField(u'CPF ou CNPJ', max_length=100)
    endereco = models.CharField(u'Endereço', max_length=200)
    numero = models.CharField(u'Número do Endereço', max_length=15)
    complemente = models.CharField(u'Complemento', max_length=250)
    bairro = models.CharField(u'Bairro', max_length=150)
    cidade = models.CharField(u'Cidade', max_length=150)
    estado = models.CharField(u'Estado', max_length=2)
    cep = models.CharField(u'CEP', max_length=10)
    pais = models.CharField(u'Pais', max_length=3)
    ddd_telefone = models.CharField(u'Código de Àrea', max_length=2)
    telefone = models.CharField(u'Número do Telefone', max_length=8)
    # não obrigatórios
    ddd_celular = models.CharField(u'Código de Àrea', max_length=2 , null=True, blank=True)
    celular = models.CharField(u'Número do Celular', max_length=8, null=True, blank=True)

    def __unicode__(self):
        return self.nome
