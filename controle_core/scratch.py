#%%

import importlib
from core.models import jobs
from core.models.objects import Alocacao, BackLog


importlib.reload(jobs)

a = Alocacao.objects.get(id_Alocacao=1)
BackLog.objects.all().delete()
jobs.create_backlog(a)


#%%

from core.models.objects import *


c = Cliente.objects.create(
    nome_cliente='Polo',
    cnpj='999999999',
    telefone='+5511999999999',
    email='polo@polo.com.br',
)

p = Pedido.objects.create(
    cliente=c,
    op='REF: COD10000001',
)

r = Referencia.objects.create(
    cliente=c,
    nome_referencia='Camisa Polo com Bolso',
)

psku = PedidoSKU.objects.create(
    pedido=p,
    referencia=r,
    quantidade=25,
)

f = Funcionario.objects.create(
    nome_funcionario='Mauricio'
)

pistola = Pistola.objects.create(
    funcionario=f,
    nome_pistola='Pistola1'
)

m = Maquina.objects.create(
    nome_maquina='Maquina de Costura'
)

acao1 = Acao.objects.create(
    maquina=m,
    nome_acao='Costura Bolso'
)

acao2 = Acao.objects.create(
    maquina=m,
    nome_acao='Costura Tronco'
)

s = Sequencia.objects.create(
    nome_sequencia='Fazer Camisa Polo Com Bolso'
)

sa1 = SequenciaAcao.objects.create(
    sequencia=s,
    acao=acao1,
    ordem_execucao=1,
    tempo_meta=1000,
)

sa2 = SequenciaAcao.objects.create(
    sequencia=s,
    acao=acao2,
    ordem_execucao=1,
    tempo_meta=1000,
)

#%%
alocacao = Alocacao.objects.create(
    pedido=p,
    referencia=r,
    sequencia=s,
    capacidade_caixa=10,
)

#%%

from core.models.objects import *


c = Caixa.objects.get(id=13)
c.render_pdf()


