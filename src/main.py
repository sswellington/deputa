#!/usr/bin/env python

from Deputa import Deputa

if __name__ == "__main__": 
    query = ((Deputa()).get_deputy({'nome': 'Rodrigo Maia'}, 'ALL'))['dados']
    print(len(query))
    query = ((Deputa()).get_all_deputy())['dados']
    print(len(query))