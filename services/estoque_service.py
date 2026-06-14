#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : estoque_service.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 12/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from repositories.estoque_repository import EstoqueRepository, CAMPOS_VALIDOS
from models.estoque import Estoque
from services.movimentacao_service import MovimentacaoService
from models.movimentacao import Movimentacao


class EstoqueService:
    def __init__(self):
        self._estoque_repository = EstoqueRepository('estoque.sqlite')
        self.movimentacao_service = MovimentacaoService()
    
    def cadastrar_estoque(self, estoque: Estoque):
        return self._estoque_repository.salvar(estoque)
    
    def atualizar_estoque(self, estoque: Estoque, id_estoque: int):
        return self._estoque_repository.atualizar(estoque, id_estoque)
    
    def deletar_estoque(self, id_estoque: int):
        return self._estoque_repository.deletar(id_estoque)

    def buscar_estoque(self, id_estoque: int):
        return self._estoque_repository.buscar_por_id(
            list(CAMPOS_VALIDOS), id_estoque
        )
    
    def listar_estoque(self):
        return self._estoque_repository.listar(
            list(CAMPOS_VALIDOS)
        )
    
    def entrada_estoque(self, estoque: Estoque, quantidade: int,
                        movimentacao: Movimentacao):

        estoque.adiciona_quantidade(quantidade)
        self.atualizar_estoque(estoque, estoque.id)
        self.movimentacao_service.cadastrar_movimentacao(movimentacao)
    
    def saida_estoque(self, estoque: Estoque, quantidade: int,
                        movimentacao: Movimentacao):
        estoque.remover_quantidade(quantidade)
        self.atualizar_estoque(estoque, estoque.id)
        self.movimentacao_service.cadastrar_movimentacao(movimentacao)

