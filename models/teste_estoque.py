#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : teste_estoque.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 07/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from produto import Produto
from fornecedor import Fornecedor
from estoque import Estoque

forn = Fornecedor("Empresa teste",
                  "023.107.662-24",
                  "teste@gmail.com",
                  "000000000000000",
                  "Avenida teste",
                  "Porto Velho",
                  "RO"
                  )
prod = Produto("Livro",
               "Livro de teste",
               "0anboabxoanefonm",
               50, True, 70,
               "Consumo",
               forn.nome)

estq = Estoque(prod,
               10, 5,
               "Prateleira 2")
# print(forn)
# print(prod)
print(estq)
