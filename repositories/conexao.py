#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : conexao.py
Description: Essa é a interface de conexão base
             para o banco de dados. Conforme o
             conforme a necessidade mais conexões
             seram adicionadas.
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 04/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from abc import ABC, abstractmethod
import sqlite3


class ConexaoBanco(ABC):

    @abstractmethod
    def conectar(self):
        pass


class ConexaoSqlite(ConexaoBanco):

    def __init__(self, nome_banco: str):
        self._nome_banco = nome_banco

    @property
    def nome_banco(self):
        return self._nome_banco

    def conectar(self, sql: str):
        with sqlite3.connect(self._nome_banco) as conexao:
            with conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    return rows
    #    try:
    #        return sqlite3.connect(self.nome_banco)
    #    except sqlite3.Error as erro:
    #        raise RuntimeError(f"Erro ao conectar ao banco: {erro}")
