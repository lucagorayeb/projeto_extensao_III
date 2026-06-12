#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : movimentacao.py
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
from .usuario import Usuario
from enum import Enum
from datetime import datetime


class Movimentacao:

    def __init__(self, produto: Produto,
                 fornecedor: Fornecedor | None,
                 tipo: TipoMovimentacao,
                 quantidade: int,
                 observacao: str | None,
                 usuario: Usuario,
                 id: int | None = None):

        self._produto = produto
        self._fornecedor = fornecedor
        self._tipo = tipo
        self._quantidade = quantidade
        self._observacao = (observacao.strip() if observacao else None)
        self._usuario = usuario
        self._data_movimentacao = datetime.now()
        self._id = id

        if quantidade <= 0:
            raise ValueError("""A quantidade deve ser maior zero.""")

        if not isinstance(tipo, TipoMovimentacao):
            raise ValueError("Tipo de movimentacao inválido.")

        if tipo == TipoMovimentacao.ENTRADA and fornecedor is None:
            raise ValueError("Entradas precisam de fornecedor.")

    def __str__(self):
        return (
                f"""Movimentação(
                produto: {self.produto.nome},
                tipo: {self.tipo.value},
                quantidade: {self.quantidade},
                movimentador: {self.usuario.nome},
                data: {self.data_movimentacao}
                )"""
            )

    @property
    def produto(self) -> Produto:
        return self._produto

    @property
    def fornecedor(self) -> Fornecedor | None:
        return self._fornecedor

    @property
    def tipo(self) -> TipoMovimentacao:
        return self._tipo

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @property
    def observacao(self) -> str | None:
        return self._observacao

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def data_movimentacao(self) -> datetime:
        return self._data_movimentacao


class TipoMovimentacao(Enum):
    ENTRADA = "entrada"
    SAIDA = "saída"
    AJUSTE = "ajuste"
