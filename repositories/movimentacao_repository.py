#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : movimentacao_repository.py
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
from models.movimentacao import Movimentacao
from typing import Any

CAMPOS_VALIDOS = {
    "id",
    "produto_id",
    "fornecedor_id",
    "tipo",
    "quantidade",
    "observacao",
    "usuario_id"
}


class MovimentacaoRepository:

    def __init__(self, conexao: str):
        self._conexao = ConexaoSqlite(conexao)

    def salvar(self, movimentacao: Movimentacao) -> int:
        sql = """INSERT INTO movimentacao (
                        produto_id,
                        fornecedor_id,
                        tipo,
                        quantidade,
                        observacao,
                        usuario_id,
                        data_movimentacao
                        ) VALUES (?, ?, ?, ?, ?, ?, ?);"""

        campos = self._obter_campos_movimentacao(movimentacao)
        print(campos)
        print(len(campos))
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, campos)
            con.commit()
            return cursor.lastrowid

    def atualizar(self, movimentacao: Movimentacao, id: int) -> int:
        sql = """UPDATE movimentacao
                 SET    produto_id = ?,
                        fornecedor_id = ?,
                        tipo = ?,
                        quantidade = ?,
                        observacao = ?,
                        usuario_id = ?,
                        data_movimentacao = ?
                   WHERE
                        id = ?;"""
        campos = self._obter_campos_movimentacao(movimentacao)
        campos.append(id)
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, campos)
            con.commit()
            return cursor.rowcount

    def deletar(self, id: int) -> int:
        sql = "DELETE FROM movimentacao WHERE id = ?;"
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, (id,))
            con.commit()
            return cursor.rowcount

    def buscar_por_id(self, campos: list[str], id: int) -> tuple | None:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM movimentacao WHERE id = ?;"
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, (id,))
            return cursor.fetchone()

    def listar(self, campos: list[str]) -> list[tuple]:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM movimentacao;"

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

    def _obter_campos_movimentacao(self,
                                   movimentacao: Movimentacao) -> list[Any]:
        return [
                movimentacao.produto,
                movimentacao.fornecedor
                if movimentacao.fornecedor else None,
                movimentacao.tipo.value,
                movimentacao.quantidade,
                movimentacao.observacao,
                movimentacao.usuario,
                str(movimentacao.data_movimentacao)
            ]
