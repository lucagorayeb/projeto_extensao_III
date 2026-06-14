#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : fornecedor_service.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 12/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from repositories.fornecedor_repository import FornecedorRepository, CAMPOS_VALIDOS
from models.fornecedor import Fornecedor 


class FornecedorService:
    def __init__(self):
        self._fornecedor_repository = FornecedorRepository('estoque.sqlite')
    
    def cadastrar_fornecedor(self, fornecedor: Fornecedor):
        return self._fornecedor_repository.salvar(fornecedor)
    
    def atualizar_fornecedor(self, fornecedor: Fornecedor, id_fornecedor: int):
        return self._fornecedor_repository.update(fornecedor, id_fornecedor)
    
    def deletar_fornecedor(self, id_fornecedor: int):
        return self._fornecedor_repository.delete(id_fornecedor)

    def buscar_fornecedor(self, id_fornecedor: int):
        return self._fornecedor_repository.buscar_por_id(
            list(CAMPOS_VALIDOS), id_fornecedor
        )
    
    def listar_fornecedor(self):
        return self._fornecedor_repository.listar(
            list(CAMPOS_VALIDOS)
        )