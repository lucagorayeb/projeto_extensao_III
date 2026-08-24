
"""
-----------------------------------------------------
Program    : conexao.py
Description: Essa é a interface de conexão base
             para o banco de dados. Conforme o
             conforme a necessidade de mais conexões
             serão adicionadas.
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 04/06/2026
Licence   : GNU/GPL v3.0
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

    def conectar(self):
        con = sqlite3.connect(self._nome_banco)
        con.execute("PRAGMA foreign_keys = ON")
        return con 

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._nome_banco:
            self._nome_banco.close()
        return False