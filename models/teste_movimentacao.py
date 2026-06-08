#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : teste_movimentacao.py
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
from movimentacao import Movimentacao, TipoMovimentacao
from usuario import Usuario
from produto_fornecedor import ProdutoFornecedor


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

user = Usuario("Luca Siqueira Assis Gorayeb de Mello")

mov = Movimentacao(prod,
                   forn.nome,
                   TipoMovimentacao.ENTRADA,
                   10,
                   "compra de teste",
                   user)

prod_forn = ProdutoFornecedor(prod, forn)

print(prod_forn)
