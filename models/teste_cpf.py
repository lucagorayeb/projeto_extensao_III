#!/usr/bin/env python 
"""
-----------------------------------------------------
Program    : teste_cpf.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 06/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from validacao_cpf_cnpj import Validadora

cpf = "023.107.662-24"
cnpj = "32.955.058/0001-85"
objeto = Validadora()
validar_cpf = objeto.validar_documento(cpf)
validar_cnpj = objeto.validar_documento(cnpj)
print(validar_cpf)
print(validar_cnpj)
