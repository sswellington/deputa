#!/usr/bin/env python
""" Deputa: auxilia o acesso a API da câmara dos deputados
    * o método get_all_deputy para acessar a lista de todos os deputados
    * o método get_deputy para acessar apenas um deputado, 
        tendo que informar parâmetro que permita localiza-lo na base de dados e 
        outro contendo a coluna que deseja ou todas.
    Source of API: https://dadosabertos.camara.leg.br/
"""
import logging
import json
import requests

from Library import Frame


class Deputa(Frame):
    def __init__(self):
        logging.basicConfig(filename=('log/deputa.txt'),
                            level=logging.DEBUG, 
                            format=' %(asctime)s - %(levelname)s - %(message)s')
        super().__init__()
        self.verb = 'GET'
        self.url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
    
    
    def get_deputy(self, query, column):
        response = requests.request(self.verb, self.url, params=query)
        if column.upper() == 'ALL':
            return json.loads(response.text)
        else:
            return (json.loads(response.text))[column]
    
    
    def get_all_deputy(self):
        response = requests.request(self.verb, self.url, params={})
        return json.loads(response.text)
    