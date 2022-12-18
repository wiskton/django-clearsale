# coding: utf-8
import urllib
from clearsale.models import Pedido, PedidoItem, Cobranca, Entrega

def clearsale(producao, codigoIntegracao, e, c, pedido):

    if producao == True:
        url = 'http://www.clearsale.com.br/integracaov2/freeclearsale/frame.aspx'
    else:
        url = 'http://homologacao.clearsale.com.br/integracaov2/freeclearsale/frame.aspx'

    VARS = {
            # CODIGO INTEGRACAO
            'CodigoIntegracao': codigoIntegracao,

            # ENTREGA
            'Entrega_Nome': e.nome,
            'Entrega_Email': e.email,
            'Entrega_Documento': e.documento,
            'Entrega_Logradouro': e.endereco,
            'Entrega_Logradouro_Numero': e.numero,
            'Entrega_Logradouro_Complemento': e.complemente,
            'Entrega_Bairro': e.bairro,
            'Entrega_Cidade': e.cidade,
            'Entrega_Estado': e.estado,
            'Entrega_CEP': e.cep,
            'Entrega_Pais': e.pais,
            'Entrega_DDD_Telefone': e.ddd_telefone,
            'Entrega_Telefone': e.telefone,
            'Entrega_DDD_Celular': e.ddd_celular, # não obrigatório
            'Entrega_Celular': e.celular, # não obrigatório

            # COBRANCA
            'Cobranca_Nome': c.nome,
            'Cobranca_Email': c.email,
            'Cobranca_Documento': c.documento,
            'Cobranca_Logradouro': c.endereco,
            'Cobranca_Logradouro_Numero': c.numero,
            'Cobranca_Logradouro_Complemento': c.complemente,
            'Cobranca_Bairro': c.bairro,
            'Cobranca_Cidade': c.cidade,
            'Cobranca_Estado': c.estado,
            'Cobranca_CEP': c.cep,
            'Cobranca_Pais': c.pais,
            'Cobranca_DDD_Telefone': c.ddd_telefone,
            'Cobranca_Telefone': c.telefone,
            'Cobranca_DDD_Celular': c.ddd_celular, # não obrigatório
            'Cobranca_Celular': c.celular, # não obrigatório

            # PEDIDO
            'PedidoID': pedido.pedido_id,
            'Data': pedido.data,
            'Total': pedido.total,
            'TipoPagamento': pedido.tipo_pagamento,
            'Parcelas': pedido.parcelas
        }

    # ITENS DO PEDIDO
    i = 1
    pedidos_item = PedidoItem.objects.filter(pedido=pedido)
    for item in pedidos_item:
        VARS['Item_ID_{0}'.format(i)] = item.item_id
        VARS['Item_Nome_{0}'.format(i)] = item.item_nome
        VARS['Item_Qtd_{0}'.format(i)] = item.item_qtd
        VARS['Item_Valor_{0}'.format(i)] = item.item_valor
        VARS['Item_Categoria_{0}'.format(i)] = item.item_categoria
        i += 1

    params = urllib.urlencode(VARS)
    f = urllib.urlopen(url, params)

    # trata pegar risco
    retorno = f.read()
    if retorno.find('<span>Baixo</span>'):
        return 'baixo'

    print retorno
    return False

def atualizar_status(producao, codigoIntegracao, pedido, status):

    retorno = False

    if producao == True:
        url = 'http://clearsale.com.br/integracaov2/FreeClearSale/AlterarStatus.aspx'
    else:
        url = 'http://homologacao.clearsale.com.br/integracaov2/FreeClearSale/AlterarStatus.aspx'

    VARS = {
            'CodigoIntegracao': codigoIntegracao,
            'PedidoID': pedido,
            'Status': status
        }

    params = urllib.urlencode(VARS)
    f = urllib.urlopen(url, params)

    # trata pegar risco
    retorno = f.read()
    if retorno.find('<body>0|OK</body>'):
        return 'sucesso'

    # return retorno
    return retorno
