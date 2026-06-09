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
from conexao import ConexaoSqlite
from projeto_extensao.models.produto import Produto


class ProdutoRepository:

    def __init__(self):
        self.con = ConexaoSqlite("teste.sql")

    def salvar(self):
        self.con.connectar("""CREATE TABLE teste(id int not null,
                           nome text not null);""")

        def buscar_por_id(self, id: int):
            pass

        def listar(self):
            pass

        def atualizar(self, produto: Produto):
            pass

        def deletar(self, id: int):
            pass
