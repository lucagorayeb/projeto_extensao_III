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

produto3 = Produto(
    nome="Monitor Full HD 24",
    descricao="Monitor LED 24 polegadas Full HD",
    codigo_barra="7891234567890",
    preco_custo=450.0,
    vendivel=True,
    preco_venda=699.90,
    categoria="Monitores"
)

produto4 = Produto(
    nome="Mouse Sem Fio",
    descricao="Mouse óptico sem fio 1600 DPI",
    codigo_barra="7894561237890",
    preco_custo=35.0,
    vendivel=True,
    preco_venda=59.90,
    categoria="Periféricos"
)

repo = ProdutoRepository("banco.sqlite")
id = 1
nome = 'Luca'

# repo.salvar(produto)
# repo.salvar(produto2)
# repo.salvar(produto3)
# repo.salvar(produto4)
# repo.atualizar(produto3, 3)
repo.deletar(4)
array = ('id', 'nome', 'descricao', 'preco_custo', 'preco_venda')
print(repo.listar(array))
# print(repo.buscar_por_id(array, 1))
