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

    def salvar(self, produto: Produto):
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

        self._executar_query_sem_retorno(sql, campos, 0)

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

        return self._executar_query_sem_retorno(sql, campos, 1)

    def deletar(self, id: int):
        sql = "DELETE FROM produto WHERE id = ?;"
        campos = [id]
        self._executar_query_sem_retorno(sql, campos, 1)

    def _executar_query_sem_retorno(self, sql: str,
                                    campos: list,
                                    verificador_retorno: int) -> int:
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql, campos)
            con.commit()
            if verificador_retorno == 0:
                return cursor.lastrowid
            return cursor.rowcount

    def _obter_campos_produto(self, produto: Produto):
        return [produto.nome,
                produto.descricao,
                produto.codigo_barra,
                produto.preco_custo,
                produto.vendivel,
                produto.preco_venda,
                produto.categoria]

    def buscar_por_id(self, campos: list[str], id: int) -> Produto | None:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        campos = [string, id]
        sql = f"SELECT {string} FROM produto WHERE id = ?;"
        return self. _executar_query_com_retorno(sql, campos, 0)

    def listar(self, campos: list[str]) -> Produto:
        self._validar_campos(campos)
        string = self._gera_campos_do_select(campos)
        campos = [string]
        sql = f"SELECT {string} FROM produto;"
        return self. _executar_query_com_retorno(sql, campos, 1)

    def _gera_campos_do_select(self, campos: list[str]) -> str:
        string = ''
        for i in range(len(campos)):
            string = f"{string} {campos[i]}"
            if i < len(campos)-1:
                string = f"{string}, "
        return string

    def _executar_query_com_retorno(self, sql: str,
                                    campos: list[str],
                                    verificador_retorno: int) -> list[tuple]:
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql)
            if verificador_retorno == 0:
                return cursor.fetchone()
            return cursor.fetchall()

    def _validar_campos(self, campos: list):
        for campo in campos:
            if campo not in CAMPOS_VALIDOS:
                raise ValueError(f"Campo inválido: {campo}")
