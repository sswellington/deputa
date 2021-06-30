#!/usr/bin/env python

from Deputa import Deputa

if __name__ == "__main__": 
    query = (Deputa()).get_deputy({'nome': 'Rodrigo Maia'}, 'dados')
    print((query))
    query = ((Deputa()).get_all_deputy())['dados']
    print('Total de deputados:', len(query))
    