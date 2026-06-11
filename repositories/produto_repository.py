#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produto_repository.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 09/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from .conexao import ConexaoSqlite
from models.produto import Produto
import sqlite3

CAMPOS_VALIDOS = {
    "id",
    "nome",
    "descricao",
    "codigo_barra",
    "preco_custo",
    "vendivel",
    "preco_venda",
    "categoria"
}


class ProdutoRepository:

    def __init__(self, conexao: str):
        self._conexao = ConexaoSqlite(conexao)

    def salvar(self, produto: Produto) -> int:
        sql = """INSERT INTO produto (
                           nome,
                           descricao,
                           codigo_barra,
                           preco_custo,
                           vendivel,
                           preco_venda,
                           categoria
                           ) VALUES (?, ?, ?, ?, ?, ?, ?);"""

        campos = self._obter_campos_produto(produto)

        cursor = self._executar_query(sql, campos)
        return cursor.lastrowid

    def atualizar(self, produto: Produto, id: int) -> int:
        sql = """UPDATE produto
                  SET    nome = ?,
                        descricao = ?,
                        codigo_barra = ?,
                        preco_custo = ?,
                        vendivel = ?,
                        preco_venda = ?,
                        categoria = ?
                   WHERE
                        id = ?;"""
        campos = self._obter_campos_produto(produto)
        campos.append(id)

        cursor = self._executar_query(sql, campos)
        return cursor.rowcount

    def deletar(self, id: int) -> int:
        sql = "DELETE FROM produto WHERE id = ?;"
        cursor = self._executar_query(sql, [id])
        return cursor.rowcount

    def _obter_campos_produto(self, produto: Produto) -> list:
        return [
                produto.nome,
                produto.descricao,
                produto.codigo_barra,
                produto.preco_custo,
                produto.vendivel,
                produto.preco_venda,
                produto.categoria
                ]

    def buscar_por_id(self, campos: list[str], id: int) -> list[tuple] | None:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM produto WHERE id = ?;"
        cursor = self._executar_query(sql, [id])
        return cursor.fetchone()

    def listar(self, campos: list[str]) -> list[tuple]:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM produto;"
        cursor = self. _executar_query(sql)
        return cursor.fetchall()

    def _validar_campos(self, campos: list) -> ValueError | None:
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

    def _executar_query(self, sql: str, campos: list = []) -> sqlite3:
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, campos)
            con.commit()
            return cursor
