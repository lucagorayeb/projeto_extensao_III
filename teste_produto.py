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
from models import Produto
from repositories import ProdutoRepository


produto = Produto(nome="Mouse Gamer",
                  descricao="Mouse RGB",
                  codigo_barra="123456789",
                  preco_custo=50.0,
                  vendivel=True,
                  preco_venda=100.0,
                  categoria="Periféricos")

produto2 = Produto(nome="Teclado Gamer",
                   descricao="Teclado RGB",
                   codigo_barra="987654321",
                   preco_custo=70.0,
                   vendivel=True,
                   preco_venda=120.0,
                   categoria="Periféricos")

repo = ProdutoRepository("banco.sqlite")
id = 1
nome = 'Luca'
# repo.salvar(produto2)
array = ('nome', 'descricao', 'preco_custo', 'preco_venda')
print(repo.listar(array))
print(repo.buscar_por_id(array, 1))
