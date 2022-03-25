#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:32:57 2022

@author: cafe
"""

# Estruturas de dados
# Listas

# A lista é ordenada, por isso é fácil acessar seus elementos em ordem, um processo chamado iterar pela lista
nomes = ["Álvaro", "Bernardo", "Beatriz"]

nomes[0] # Acessando elementos de uma lista
for nome in nomes: # Definindo um laço for
    print(nome)


# Controle de fluxo é o processo de determinar o fluxo de operações ou seja a ordem e repetições
for nome in nomes: # Definindo um laço for
    if nome == "Álvaro":
        print(f"Bom dia, professor {nome}")
    else:
        print(f"Bom dia, {nome}")
