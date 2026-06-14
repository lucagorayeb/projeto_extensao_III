#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produto_fornecedor_service.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from repositories.produto_fornecedor_repository import ProdutoFornecedorRepository, CAMPOS_VALIDOS
from models.produto_fornecedor import ProdutoFornecedor


class ProdutoFornecedorService:
    def __init__(self):
        self._produto_fornecedor_repository = ProdutoFornecedorRepository('estoque.sqlite')
    
    def cadastrar_produto_fornecedor(self, produto_fornecedor: ProdutoFornecedor):
        return self._produto_fornecedor_repository.salvar(produto_fornecedor)
    
    def atualizar_produto_fornecedor(self, produto_fornecedor: ProdutoFornecedor, id_produto_fornecedor: int):
        return self._produto_fornecedor_repository.atualizar(produto_fornecedor, id_produto_fornecedor)
    
    def deletar_produto_fornecedor(self, id_produto_fornecedor: int):
        return self._produto_fornecedor_repository.deletar(id_produto_fornecedor)

    def buscar_produto_fornecedor(self, id_produto_fornecedor: int):
        return self._produto_fornecedor_repository.buscar_por_id(
            list(CAMPOS_VALIDOS), id_produto_fornecedor
        )
    
    def listar_produto_fornecedor(self):
        return self._produto_fornecedor_repository.listar(
            list(CAMPOS_VALIDOS)
        ) 