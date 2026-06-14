#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : movimentacao_service.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from repositories.movimentacao_repository import MovimentacaoRepository, CAMPOS_VALIDOS
from models.movimentacao import Movimentacao


class MovimentacaoService:
    def __init__(self):
        self._movimentacao_repository = MovimentacaoRepository('estoque.sqlite')
    
    def cadastrar_movimentacao(self, movimentacao: Movimentacao):
        return self._movimentacao_repository.salvar(movimentacao)
    
    def atualizar_movimentacao(self, movimentacao: Movimentacao, id_movimentacao: int):
        return self._movimentacao_repository.atualizar(movimentacao, id_movimentacao)
    
    def deletar_movimentacao(self, id_movimentacao: int):
        return self._movimentacao_repository.deletar(id_movimentacao)

    def buscar_movimentacao(self, id_movimentacao: int):
        return self._movimentacao_repository.buscar_por_id(
            list(CAMPOS_VALIDOS), id_movimentacao
        )
    
    def listar_movimentacao(self):
        return self._movimentacao_repository.listar(
            list(CAMPOS_VALIDOS)
        )
    
    def listar_movimentacoes_produto(self, id_produto: int):
        pass