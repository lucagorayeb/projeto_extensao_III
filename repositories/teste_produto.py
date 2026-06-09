#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : teste_produto.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 06/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from models.produto import Produto
from produto_repository import ProdutoRepository


produto = Produto(nome="Mouse Gamer",
                  descricao="Mouse RGB",
                  codigo_barra="123456789",
                  preco_custo=50.0,
                  vendivel=True,
                  preco_venda=100.0,
                  categoria="Periféricos")

repo = ProdutoRepository()
repo.salvar()
