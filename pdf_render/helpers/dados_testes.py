from helpers import jobs, functions


def informacao_caixa():
    data = {'header': {'nome_cliente': 'Polo',
                       'nome_caixa': 1,
                       'pedido_op': 'REF: COD10000001',
                       'referencia_id': 1,
                       'nome_referencia': 'Camisa Polo com Bolso',
                       'nome_sequencia': 'Fazer Camisa Polo Com Bolso'
                       },
            'body': [{'maquina': 'Maquina de Costura',
                      'ordem_execucao': '1',
                      'nome_acao': 'Costura Bolso',
                      'tempo_medio': '1000',
                      'cod_bar': 987654321,
                      # 'cod_bar_address': '{}'.format(jobs.create_barcode(987654321)),
                      'cod_bar_address': functions.path2url('static/{}'.format(jobs.create_barcode(987654321))),
                      },
                     {'maquina': 'Maquina de Costura',
                      'ordem_execucao': '2',
                      'nome_acao': 'Costura Tronco',
                      'tempo_medio': '1000',
                      'cod_bar': 123456789,
                      # 'cod_bar_address': '{}'.format(jobs.create_barcode(123456789)),
                      'cod_bar_address': functions.path2url('static/{}'.format(jobs.create_barcode(123456789))),
                      },
                      {'maquina': 'Maquina de Costura',
                      'ordem_execucao': '1',
                      'nome_acao': 'Costura Bolso',
                      'tempo_medio': '1000',
                      'cod_bar': 987654321,
                      # 'cod_bar_address': '{}'.format(jobs.create_barcode(987654321)),
                      'cod_bar_address': functions.path2url('static/{}'.format(jobs.create_barcode(987654321))),
                      }
                     ]
            }
    return data
