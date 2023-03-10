django-clearsale
================

Integração com clearsale

Clear Sale possui duas urls uma para homologação outra para produção, caso utilize a url para teste de homologação é preciso fazer o cadastro também igual de produção no link <a href="http://homologacao.clearsale.com.br/loja/Cadastro.aspx" target="blank">aqui</a>.

Instalar no env::

    pip install -e git+git@github.com:willemallan/django-clearsale.git#egg=django-clearsale

Adicionar em INSTALLED_APPS no settings.py::

    INSTALLED_APPS = (
        'clearsale',
        'requests',
    )

Views::

    def retorno(request):

        ### INICIO CLEARSALE

        # BANDEIRA CARTÃO
        # 1 Diners
        # 2 MasterCard
        # 3 Visa
        # 4 Outros
        # 5 American Express
        # 6 HiperCard
        # 7 Aura

        # TIPO DE PAGAMENTO
        # 1 Cartão de Crédito
        # 2 Boleto Bancário
        # 3 Débito Bancário
        # 4 Débito Bancário – Dinheiro
        # 5 Débito Bancário – Cheque
        # 6 Transferência Bancária
        # 7 Sedex a Cobrar
        # 8 Cheque
        # 9 Dinheiro
        # 10 Financiamento
        # 11 Fatura
        # 12 Cupom
        # 13 Multicheque
        # 14 Outros

        # TIPOS DE RETORNO
        # CAN – Cancelado pelo cliente
        # SUS – Suspeito
        # APM – Aprovado
        # FRD – Fraude Confirmada
        # RPM – Reprovado

        producao = False
        retorno = None
        codigoIntegracao = ''

        # dados de entrega
        entrega = Entrega()
        entrega.nome = 'Goku'
        entrega.email = 'goku@gmail.com'
        entrega.documento = '99999999999'
        entrega.endereco = 'Rua Namekusei'
        entrega.numero = '9999'
        entrega.complemente = 'casa'
        entrega.bairro = 'Jardim DBZ'
        entrega.cidade = 'Namekusei'
        entrega.estado = 'SP'
        entrega.cep = '34000999'
        entrega.pais = 'Brasil'
        entrega.ddd_telefone = '99'
        entrega.telefone = '999999999'
        # não obrigatórios
        entrega.ddd_celular = '16'
        entrega.celular = '999999999'

        # dados de cobranca
        cobranca = Cobranca()
        cobranca.nome = 'Goku'
        cobranca.email = 'goku@gmail.com'
        cobranca.documento = '99999999999'
        entrega.endereco = 'Rua Namekusei'
        cobranca.numero = '9999'
        cobranca.complemente = 'casa'
        cobranca.bairro = 'Jardim DBZ'
        cobranca.cidade = 'Namekusei'
        cobranca.estado = 'SP'
        cobranca.cep = '999999999'
        cobranca.pais = 'Brasil'
        cobranca.ddd_telefone = '99'
        cobranca.telefone = '999999999'
        # não obrigatórios
        cobranca.ddd_celular = '99'
        cobranca.celular = '999999999'

        # dados do pedido
        pedido = Pedido()
        pedido.pedido_id = '11321'
        pedido.data = '26-02-2013 15:39:21'
        pedido.total = 1
        pedido.tipo_pagamento = 1
        pedido.parcelas = 1
        # não obrigatórios
        pedido.tipo_cartao = 1
        pedido.ip = '100100100'
        # CASO RISCO SEJA ALTO DEIXAR - PENDENTE
        # pedido.status = 'PEN'
        pedido.save()

        # for nos itens do pedido
        for i in range(0,3):
            pedido_item = PedidoItem()
            pedido_item.pedido = pedido
            pedido_item.item_id = '123'
            pedido_item.item_nome = 'Suco TOP'
            pedido_item.item_qtd = 10
            pedido_item.item_valor = 50.0
            pedido_item.item_categoria = 'Suco'
            pedido_item.save()

        # parametros (Producao, codigoIntegracao, entrega, cobranca, pedido)
        retorno = clearsale(producao, codigoIntegracao, entrega, cobranca, pedido)

        # SALVA O RETORNO - STATUS DO PEDIDO
        pedido.status = retorno
        if retorno == 'baixo':

            # APROVADO
            status = 'APM'

            # ATUALIZA
            retorno = atualizar_status(producao, codigoIntegracao, pedido.pedido_id, status)
            if retorno == 'sucesso':
                # SALVA O RETORNO - STATUS DO PEDIDO
                # pedido = get_object_or_404(Pedido, pedido_id=pedido)
                pedido = Pedido.objects.filter(pedido_id=pedido)
                if pedido:
                    pedido = pedido[0]
                pedido.status = status
                pedido.save()
            else:
                retorno = 'erro'
        else:
            # pendente risco diferente de baixo
            pedido.status = 'PEN'
            pedido.save()


        pedido.save()

        ### FIM CLEARSALE

        VARS = {
                'clearsale': retorno,
        }

        return render_to_response('home.html', VARS, context_instance=RequestContext(request))

    def atualiza_status(request):

        codigoIntegracao = ''
        pedido = '11320'
        status = u'APM'
        retorno = None
        producao = False

        # parametros (Producao, codigoIntegracao, entrega, cobranca, pedido)
        retorno = atualizar_status(producao, codigoIntegracao, pedido, status)
        if retorno == 'sucesso':
            # SALVA O RETORNO - STATUS DO PEDIDO
            # pedido = get_object_or_404(Pedido, pedido_id=pedido)
            pedido = Pedido.objects.filter(pedido_id=pedido)
            if pedido:
                pedido = pedido[0]
            pedido.status = status
            pedido.save()
        else:
            retorno = 'erro'

        ### FIM CLEARSALE

        VARS = {
                'clearsale': retorno,
        }

        return render_to_response('home.html', VARS, context_instance=RequestContext(request))

urls.py::

    from django.conf.urls import patterns, include, url

    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        url(r'^clearsale/$', 'djangoclearsale.views.retorno', name='retorno'),
        url(r'^atualizar/$', 'djangoclearsale.views.atualiza_status', name='atualizar'),
    )

templates/home.html::

    {{ clearsale|safe }}
#
