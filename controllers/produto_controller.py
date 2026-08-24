
"""
-----------------------------------------------------
Program    : produto_controller.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Licence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from services.produto_service import ProdutoService
from dto.produto_request import ProdutoRequest
from models.produto import Produto

produto_service = ProdutoService()

class ProdutoController:
    def __init__(self) -> None:
        self._produto_service = ProdutoService()

    def listar_produtos(self)  -> None:
        return self._produto_service.listar_produto()

    def buscar_produto(self, id_produto: int):
        return self._produto_service.buscar_produto(id_produto)

    def cadastrar_produto(self, dados: ProdutoRequest) -> None:
        produto = Produto(
            nome = dados.nome,
            descricao = dados.descricao,
            codigo_barra = dados.codigo_barra,
            preco_custo = dados.preco_custo,
            vendivel = dados.vendivel,
            preco_venda = dados.preco_venda,
            categoria = dados.categoria
        )

        self._produto_service.cadastrar_produto(produto)

    def atualizar_produto(self, dados: ProdutoRequest, id_produto: int) -> None:
        produto = Produto(
            nome = dados.nome,
            descricao = dados.descricao,
            codigo_barra = dados.codigo_barra,
            preco_custo = dados.preco_custo,
            vendivel = dados.vendivel,
            preco_venda = dados.preco_venda,
            categoria = dados.categoria
        )

        self._produto_service.atualizar_produto(produto, id_produto)

    def deletar_produto(self, id_produto: int) -> None:
        self._produto_service.deletar_produto(id_produto)

