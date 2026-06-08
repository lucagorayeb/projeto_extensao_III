#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : estoque.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 06/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from produto import Produto


class Estoque:
    def __init__(self, produto: Produto,
                 quantidade: int,
                 quantidade_minima: int,
                 localizacao: str,
                 id: int | None = None):

        self._produto = produto
        self._quantidade = quantidade
        self._quantidade_minima = quantidade_minima
        self._localizacao = localizacao
        self._id = id

        if quantidade_minima <= 0 or quantidade <= 0:
            raise ValueError("""Quantidades não
                             podem ser zero ou negativa.""")

        self._verifica_localizacao_vazia(localizacao)

    def __str__(self):
        return (
                f"""Estoque (
                produto: {self.produto.nome}
                quantidade: {self.quantidade}
                quantidade minima: {self.quantidade_minima}
                localização: {self.localizacao}
                )"""
                )

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def produto(self) -> Produto:
        return self._produto

    @property
    def quantidade(self) -> int:
        return self._quantidade

    def adiciona_quantidade(self, quantidade: int):
        self._verifica_se_quantidade_eh_valida(quantidade)
        self._quantidade = self._quantidade + quantidade

    def remover_quantidade(self, quantidade: int):
        self._verifica_se_quantidade_eh_valida(quantidade)

        if self._quantidade < quantidade:
            raise ValueError(f"""
                            Quantida do estoque inferior a {quantidade}.
                             """)
        self._quantidade = self._quantidade - quantidade

    @property
    def quantidade_minima(self) -> int:
        return self._quantidade_minima

    def aumentar_quantidade_minima(self, quantidade: int):
        self._verifica_se_quantidade_eh_valida(quantidade)
        self._quantidade_minima = self._quantidade_minima + quantidade

    def diminuir_quantidade_minima(self, quantidade: int):
        self._verificar_se_quantidade_minima_zerou(quantidade)
        self._quantidade_minima = self._quantidade_minima - quantidade

    def _verificar_se_quantidade_minima_zerou(self, quantidade):
        total = self._quantidade_minima - quantidade
        if total <= 0:
            raise ValueError("""Quantidade mínima não
                            pode ser zero ou negativa.""")

    def _verifica_se_quantidade_eh_valida(self, quantidade: int):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida.")

    @property
    def precisa_reposicao(self) -> bool:
        return self._quantidade <= self.quantidade_minima

    @property
    def localizacao(self) -> str:
        return self._localizacao

    def alterar_localizacao(self, nova_localizacao):
        self._verifica_localizacao_vazia(nova_localizacao)
        self._localizacao = nova_localizacao

    def _verifica_localizacao_vazia(self, localizacao: str):
        if not localizacao.strip():
            raise ValueError("Todos os campos devem ser preechidos.")
