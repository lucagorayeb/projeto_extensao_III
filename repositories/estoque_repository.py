#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : estoque_repository.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 11/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from .conexao import ConexaoSqlite
from models.estoque import Estoque
from typing import Any

CAMPOS_VALIDOS = {
    "id",
    "produto_id",
    "quantidade",
    "quantidade_minima",
    "localizacao"
}


class EstoqueRepository:

    def __init__(self, conexao: str):
        self._conexao = ConexaoSqlite(conexao)

    def salvar(self, estoque: Estoque) -> int:
        sql = """INSERT INTO estoque (
                           produto_id,
                           quantidade,
                           quantidade_minima,
                           localizacao
                           ) VALUES (?, ?, ?, ?);"""

        campos = self._obter_campos_estoque(estoque)
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, campos)
            con.commit()
            return cursor.lastrowid

    def atualizar(self, estoque: Estoque, id: int) -> int:
        sql = """UPDATE estoque
                 SET    produto_id = ?,
                        quantidade = ?,
                        quantidade_minima = ?,
                        localizacao = ?
                   WHERE
                        id = ?;"""
        campos = self._obter_campos_estoque(estoque)
        campos.append(id)
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, campos)
            con.commit()
            return cursor.rowcount

    def deletar(self, id: int) -> int:
        sql = "DELETE FROM estoque WHERE id = ?;"
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, (id,))
            con.commit()
            return cursor.rowcount

    def buscar_por_id(self, campos: list[str], id: int) -> tuple | None:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM estoque WHERE id = ?;"
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, (id,))
            return cursor.fetchone()

    def listar(self, campos: list[str]) -> list[tuple]:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM estoque;"

        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql)
            return cursor.fetchall()

    def _validar_campos(self, campos: list) -> None:
        for campo in campos:
            if campo not in CAMPOS_VALIDOS:
                raise ValueError(f"Campo inválido: {campo}")

    def _gera_campos_do_select(self, campos: list[str]) -> str:
        string = ''
        for i in range(len(campos)):
            string = f"{string} {campos[i]}"
            if i < len(campos)-1:
                string = f"{string}, "
        return string

    def _obter_campos_estoque(self, estoque: Estoque) -> list[Any]:
        return [
                estoque.produto.id,
                estoque.quantidade,
                estoque.quantidade_minima,
                estoque.localizacao
                ]
