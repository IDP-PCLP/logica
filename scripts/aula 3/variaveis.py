#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:12:09 2022

@author: cafe
"""


# Variáveis em Python são declaradas com o sinal de =

numero = 1
texto = "Olá, mundo!"
booleano = True # ou False

# Podemos atribuir resultados de funções a variáveis
nome = input("Qual é seu nome? ")
print(f"Olá, {nome}!")

continuar = True
while continuar:
    continuar = False
    nome = input("Qual é seu nome? ")
    print(f"Olá, {nome}!")
    cont = input("Continuar? ")
    if cont == "S" or cont == "s":
        continuar = True
    if cont in "SsSim":
        continuar = True
