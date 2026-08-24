
"""
-----------------------------------------------------
Program    : produto_service.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 12/06/2026
Licence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from repositories.produto_repository import ProdutoRepository, CAMPOS_VALIDOS
from models.produto import Produto 


class ProdutoService:
    def __init__(self):
        self._produto_repository = ProdutoRepository('estoque.sqlite')
    
    def cadastrar_produto(self, produto: Produto):
        return self._produto_repository.salvar(produto)
    
    def atualizar_produto(self, produto: Produto, id_produto: int):
        return self._produto_repository.atualizar(produto, id_produto)
    
    def deletar_produto(self, id_produto: int):
        return self._produto_repository.deletar(id_produto)

    def buscar_produto(self, id_produto: int):
        return self._produto_repository.buscar_por_id(
            list(CAMPOS_VALIDOS), id_produto
        )
    
    def listar_produto(self):
        return self._produto_repository.listar(
            list(CAMPOS_VALIDOS)
        )