#!/usr/bin/env python 
"""
-----------------------------------------------------
Program    : teste_fornecedor.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 06/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from fornecedor import Fornecedor

fornecedor = Fornecedor(nome="Empresa Fachada",
                        cpf_cnpj="023.107.662-24",
                        email="teste@gmail.com",
                        telefone="7777777",
                        endereco="Avenida exemplo, 734",
                        cidade="Porto Velho",
                        estado="RO")
print(fornecedor)
print(fornecedor.nome)
print(fornecedor.cpf_cnpj)
