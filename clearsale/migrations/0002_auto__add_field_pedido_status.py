# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pedido.status'
        db.add_column('clearsale_pedido', 'status',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pedido.status'
        db.delete_column('clearsale_pedido', 'status')


    models = {
        'clearsale.cobranca': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Cobranca'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'complemente': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ddd_celular': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'documento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'clearsale.entrega': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Entrega'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'complemente': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ddd_celular': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'documento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'clearsale.pedido': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Pedido'},
            'data': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'parcelas': ('django.db.models.fields.FloatField', [], {'max_length': '2'}),
            'pedido_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'tipo_cartao': ('django.db.models.fields.FloatField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'tipo_pagamento': ('django.db.models.fields.FloatField', [], {'max_length': '2'}),
            'total': ('django.db.models.fields.FloatField', [], {'max_length': '9'})
        },
        'clearsale.pedidoitem': {
            'Meta': {'ordering': "('-item_id',)", 'object_name': 'PedidoItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_categoria': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'item_nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'item_qtd': ('django.db.models.fields.FloatField', [], {'max_length': '2'}),
            'item_valor': ('django.db.models.fields.FloatField', [], {'max_length': '9'}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clearsale.Pedido']"})
        }
    }

    complete_apps = ['clearsale']