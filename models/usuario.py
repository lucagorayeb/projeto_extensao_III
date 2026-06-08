#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : usuario.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 07/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""


class Usuario:

    def __init__(self, nome: str,
                 id: int | None = None):

        self._nome = nome
        self._id = id

        self.verifica_se_nome_vazio(nome)

    def __str__(self):
        return (f"""Usuario(
               nome: {self._nome},
               )"""
                )

    @property
    def nome(self) -> str:
        return self._nome

    def alterar_nome(self, novo_nome: str):
        self.verifica_se_nome_vazio(novo_nome)
        self._nome = novo_nome

    def verifica_se_nome_vazio(self, nome):
        if not nome.strip():
            raise ValueError("Campo nome deve ser preenchido")

    @property
    def id(self) -> int | None:
        return self._id
