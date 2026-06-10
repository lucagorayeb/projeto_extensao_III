#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produtor_fornecedor.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 07/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from .produto import Produto
from .fornecedor import Fornecedor


class ProdutoFornecedor:
    def __init__(self, produto: Produto,
                 fornecedor: Fornecedor,
                 id: int | None = None):

        self._produto = produto
        self._fornecedor = fornecedor
        self._id = id

        if not isinstance(produto, Produto):
            raise TypeError("Produto inválido.")

        if not isinstance(fornecedor, Fornecedor):
            raise TypeError("Fornecedor inválido.")

    def __str__(self):
        return (f"""
                ProdutoFornecedor(
                produto: {self.produto.nome},
                fornecedor: {self.fornecedor.nome}
                )""")

    @property
    def produto(self) -> Produto:
        return self._produto

    @property
    def fornecedor(self) -> Fornecedor:
        return self._fornecedor

    @property
    def id(self) -> int | None:
        return self._id
