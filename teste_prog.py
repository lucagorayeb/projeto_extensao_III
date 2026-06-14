#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : teste_prog.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from models.produto import Produto
from models.fornecedor import Fornecedor
from models.usuario import Usuario
from models.estoque import Estoque
from models.movimentacao import Movimentacao, TipoMovimentacao

from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService
from services.usuario_service import UsuarioService
from services.estoque_service import EstoqueService
from services.movimentacao_service import MovimentacaoService


def main():

    produto_service = ProdutoService()
    fornecedor_service = FornecedorService()
    usuario_service = UsuarioService()
    estoque_service = EstoqueService()
    movimentacao_service = MovimentacaoService()

    # --------------------------------------------------
    # Cria usuário
    # --------------------------------------------------

    usuario = Usuario(
        nome="Administrador"
    )

    usuario_id = usuario_service.cadastrar_usuario(usuario)

    print(f"Usuário criado: {usuario_id}")

    # --------------------------------------------------
    # Cria fornecedor
    # --------------------------------------------------

    fornecedor = Fornecedor(
        nome="Fornecedor Teste",
        cpf_cnpj="11444777000161",
        email="fornecedor@email.com",
        telefone="69999999999",
        endereco="Rua Teste",
        cidade="Porto Velho",
        estado="RO"
    )

    fornecedor_id = fornecedor_service.cadastrar_fornecedor(
        fornecedor
    )

    print(f"Fornecedor criado: {fornecedor_id}")

    # --------------------------------------------------
    # Cria produto
    # --------------------------------------------------

    produto = Produto(
        nome="Mouse Gamer",
        descricao="Mouse RGB",
        codigo_barra="123456789",
        preco_custo=50.0,
        vendivel=True,
        preco_venda=90.0,
        categoria="Periféricos"
    )

    produto_id = produto_service.cadastrar_produto(produto)

    print(f"Produto criado: {produto_id}")

    # Se seu model possui setter ou construtor com id
    produto._id = produto_id

    # --------------------------------------------------
    # Cria estoque
    # --------------------------------------------------

    estoque = Estoque(
        produto=produto,
        quantidade=10,
        quantidade_minima=5,
        localizacao="Prateleira A"
    )

    estoque_id = estoque_service.cadastrar_estoque(
        estoque
    )

    estoque._id = estoque_id

    print(f"Estoque criado: {estoque_id}")

    # --------------------------------------------------
    # Entrada de estoque
    # --------------------------------------------------

    movimentacao_entrada = Movimentacao(
        produto=produto_id,
        fornecedor=fornecedor_id,
        tipo=TipoMovimentacao.ENTRADA,
        quantidade=20,
        observacao="Reposição de estoque",
        usuario=usuario_id
    )
    
    print(movimentacao_entrada)

    estoque_service.entrada_estoque(
        estoque,
        20,
        movimentacao_entrada
    )
    print(movimentacao_entrada)
    print(
        f"Entrada realizada. Quantidade atual: "
        f"{estoque.quantidade}"
    )

    # --------------------------------------------------
    # Saída de estoque
    # --------------------------------------------------

    movimentacao_saida = Movimentacao(
        produto=produto_id,
        fornecedor=None,
        tipo=TipoMovimentacao.SAIDA,
        quantidade=5,
        observacao="Venda realizada",
        usuario=usuario_id
    )

    print(movimentacao_saida)

    estoque_service.saida_estoque(
        estoque,
        5,
        movimentacao_saida
    )

    print(
        f"Saída realizada. Quantidade atual: "
        f"{estoque.quantidade}"
    )

    # --------------------------------------------------
    # Consulta estoque
    # --------------------------------------------------

    print("\nEstoque final:")
    print(estoque.quantidade)

    # --------------------------------------------------
    # Consulta movimentações
    # --------------------------------------------------

    movimentacoes = movimentacao_service.listar_movimentacao()

    print("\nMovimentações:")
    for mov in movimentacoes:
        print(mov)


if __name__ == "__main__":
    main()