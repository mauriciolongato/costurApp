#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.files.base import ContentFile
from django.db import models

import math
import requests
import json


# Cliente
class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=500)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=500)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return u'%s' % self.nome_cliente


# Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    op = models.CharField(max_length=5000, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return u'%s' % self.op


# Referencia
class Referencia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome_referencia = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Referencias'

    def __str__(self):
        return u'%s' % self.nome_referencia


# Pedido_SKU
class PedidoSKU(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Pedido_SKUs'


# Funcionario
class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return u'%s' % self.nome_funcionario


# Pistola
class Pistola(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE, primary_key=True, )
    nome_pistola = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Leitor de Código de Barras'
        verbose_name_plural = 'Leitores de Código de Barras'

    def __str__(self):
        return u'%s' % self.nome_pistola


# Maquina
class Maquina(models.Model):
    nome_maquina = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return u'%s' % self.nome_maquina


# Acao
class Acao(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nome_acao = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Operação'
        verbose_name_plural = 'Operações'

    def __str__(self):
        return u'%s' % self.nome_acao


# Sequencia
class Sequencia(models.Model):
    nome_sequencia = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Sequencias'

    def __str__(self):
        return u'%s' % self.nome_sequencia


# Sequencia
class SequenciaAcao(models.Model):
    sequencia = models.ForeignKey(Sequencia, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    ordem_execucao = models.CharField(max_length=500)
    tempo_padrao = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Sequencia e Operações'
        verbose_name_plural = 'Sequencias e Operações'

    def __str__(self):
        return u'%s' % self.id


# Alocacao
class Alocacao(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    sequencia = models.ForeignKey(Sequencia, on_delete=models.CASCADE)
    quantidade_referencia = models.IntegerField(blank=True)
    capacidade_caixa = models.IntegerField(blank=True)
    quantidade_caixas = models.IntegerField(blank=True)
    pdf = models.FileField(upload_to='pdf/', blank=True)

    def save(self, *args, **kwargs):
        self.quantidade_referencia = PedidoSKU.objects.get(referencia=self.referencia).quantidade
        self.quantidade_caixas = math.ceil(self.quantidade_referencia / self.capacidade_caixa)
        super(Alocacao, self).save(*args, **kwargs)
        self.create_caixas()

    def create_caixas(self):
        for caixa_id in range(self.quantidade_caixas):
            c = Caixa.objects.create(alocacao=self)
            c.create_backlog()
            c.render_pdf()
            c.save()

    class Meta:
        verbose_name_plural = 'Alocacoes'

    def __str__(self):
        return u'%s' % self.id


class Caixa(models.Model):
    alocacao = models.ForeignKey(Alocacao, on_delete=models.CASCADE)
    pedido = models.TextField(blank=True)
    referencia = models.TextField(blank=True)
    pdf = models.FileField(upload_to='pdf/', blank=True)

    def create_backlog(self):
        for sequencia_acao in self.alocacao.sequencia.sequenciaacao_set.all():
            b = BackLog.objects.create(caixa=self, sequencia_acao=sequencia_acao)
            b.resolve_backlog()
            b.save()

    def render_pdf(self):
        self.pedido = self.alocacao.pedido.op
        self.referencia = self.alocacao.referencia.nome_referencia

        body = []
        html_bloco = {}
        for backlog in self.backlog_set.all():
            header = {'nome_cliente': backlog.cliente.nome_cliente,
                      'pedido_op': backlog.pedido_op,
                      'nome_caixa': backlog.caixa.id,
                      'referencia_id': backlog.referencia_id,
                      'nome_referencia': backlog.referencia.nome_referencia,
                      'nome_sequencia': backlog.sequencia_acao.sequencia.nome_sequencia,
                      }

            row = {'maquina': backlog.sequencia_acao.acao.maquina.nome_maquina,
                   'ordem_execucao': backlog.sequencia_acao.ordem_execucao,
                   'nome_acao': backlog.sequencia_acao.acao.nome_acao,
                   'tempo_medio': backlog.sequencia_acao.tempo_padrao,
                   'cod_bar': backlog.id
                   }

            body.append(row)

            nome_maquina = backlog.sequencia_acao.acao.maquina.nome_maquina
            if nome_maquina in html_bloco:
                html_bloco[nome_maquina].append(row)
            else:
                html_bloco[nome_maquina] = [row]

        data = {'header': header, 'body': body, 'html_bloco': html_bloco}
        r = requests.post('http://localhost:5000/', data=json.dumps(data))
        self.pdf.save('test_pdf_rendering.pdf', ContentFile(r.content))

    class Meta:
        verbose_name_plural = 'Caixas'

    def __str__(self):
        return u'%s' % self.id


# BackLog
class BackLog(models.Model):
    pedido_data_criacao = models.DateTimeField(auto_now_add=True)
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
    sequencia_acao = models.ForeignKey(SequenciaAcao, on_delete=models.DO_NOTHING, null=True)
    alocacao = models.ForeignKey(Alocacao, on_delete=models.CASCADE, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True)
    referencia = models.ForeignKey(Referencia, on_delete=models.DO_NOTHING, null=True)

    pedido_op = models.TextField(blank=True)
    nome_cliente = models.TextField(blank=True)
    nome_referencia = models.TextField(blank=True)
    nome_acao = models.TextField(blank=True)
    ordem_execucao = models.IntegerField(null=True)

    def resolve_backlog(self):
        # ForeignKey
        self.alocacao = self.caixa.alocacao
        self.pedido = self.caixa.alocacao.pedido
        self.cliente = self.caixa.alocacao.pedido.cliente
        self.referencia = self.caixa.alocacao.referencia
        # Campos
        self.pedido_op = self.caixa.alocacao.pedido.op
        self.nome_cliente = self.caixa.alocacao.pedido.cliente.nome_cliente
        self.nome_referencia = self.caixa.alocacao.referencia.nome_referencia
        self.nome_acao = self.sequencia_acao.acao.nome_acao
        self.ordem_execucao = self.sequencia_acao.ordem_execucao

    class Meta:
        verbose_name_plural = 'BackLogs'


# Log_Trabalho
class LogTrabalho(models.Model):
    pistola = models.CharField(max_length=500)
    cod_barras = models.CharField(max_length=500)
    data_criacao = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Log_Trabalhos'
