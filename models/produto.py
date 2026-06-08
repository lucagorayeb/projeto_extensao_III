#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produto.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 04/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from fornecedor import Fornecedor


class Produto:
    def __init__(self, nome: str,
                 descricao: str,
                 codigo_barra: str,
                 preco_custo: float,
                 vendivel: bool,
                 preco_venda: float | None,
                 categoria: str,
                 id: int | None = None):
        self._nome = nome
        self._descricao = descricao
        self._codigo_barra = codigo_barra
        self._preco_custo = preco_custo
        self._vendivel = vendivel
        self._preco_venda = preco_venda
        self._categoria = categoria
        self._id = id

        if preco_custo < 0:
            raise ValueError("Preço de custo não pode ser negativo")
        if vendivel:
            if preco_venda is None:
                raise ValueError("""Produto vendivel precisa ter
                                 um preço de venda.""")

            if preco_venda < preco_custo:
                raise ValueError("""Preço de venda não pode ser
                                 menor que o preço de custo.""")

        campos = [nome,
                  descricao,
                  codigo_barra,
                  categoria]

        if any(not campo.strip() for campo in campos):
            raise ValueError("Todos os campos devem ser preechidos.")

    def __str__(self):
        return (
            f"""Produto (
            nome: {self.nome}
            descrição: {self.descricao}
            código de barra: {self.codigo_barra}
            preço custo: {self.preco_custo}
            vendivel: {self.vendivel}
            preço venda: {self.preco_venda}
            categoria: {self.categoria}
            )"""
        )

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def descricao(self) -> str:
        return self._descricao

    def alterar_descricao(self, nova_descricao: str):
        self._verifica_se_string_esta_vazia(nova_descricao)
        self._descricao = nova_descricao

    @property
    def codigo_barra(self) -> str:
        return self._codigo_barra

    @property
    def preco_custo(self) -> float:
        return self._preco_custo

    @property
    def vendivel(self) -> bool:
        return self._vendivel

    @property
    def preco_venda(self) -> float:
        return self._preco_venda

    def alterar_preco_venda(self, novo_preco: float):
        if not self._vendivel:
            raise ValueError("""Produtos não vendiveis não
                             podem ter preço de venda.""")

        if novo_preco < self.preco_custo:
            raise ValueError("""Preço de venda não pode ser
                             menor que o preço do custo.""")

        self._preco_venda = novo_preco

    @property
    def categoria(self) -> str:
        return self._categoria

    def alterar_categoria(self, nova_categoria: str):
        self._verifica_se_string_esta_vazia(nova_categoria)
        self._categoria = nova_categoria

    @property
    def fornecedor(self) -> Fornecedor:
        return self._fornecedor

    def _verifica_se_string_esta_vazia(self, string: str):
        if not string.strip():
            raise ValueError("Campo vazio.")
