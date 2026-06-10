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
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(
                    sql,
                    (
                        produto.nome,
                        produto.descricao,
                        produto.codigo_barra,
                        produto.preco_custo,
                        produto.vendivel,
                        produto.preco_venda,
                        produto.categoria
                    )
            )
            con.commit()

    def buscar_por_id(self, campos: list[str], id: int) -> str:
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM produto WHERE id = {id};"
        return self. _select_listagem(sql)

    def listar(self, campos: list[str]) -> str:
        string = self._gera_campos_do_select(campos)
        sql = f"SELECT {string} FROM produto;"
        return self. _select_listagem(sql)

    def _gera_campos_do_select(self, campos: list[str]) -> str:
        string = ''
        for i in range(len(campos)):
            string = f"{string} {campos[i]}"
            if i < len(campos)-1:
                string = f"{string}, "
        return string

    def _select_listagem(self, sql: str) -> str:
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
            con.commit()
            return resultado

    def atualizar(self, produto: Produto):
        pass

    def deletar(self, id: int):
        pass
