#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : teste_produto.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 06/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from models import Produto
from repositories import ProdutoRepository
from services import ProdutoService

from models import Produto, Fornecedor, ProdutoFornecedor, Usuario
from models import Movimentacao, TipoMovimentacao, Estoque 
from services import ProdutoFornecedorService, EstoqueService 
from services import FornecedorService, MovimentacaoService
from services import ProdutoService, UsuarioService

produto = Produto(nome="Mouse Gamer",
                  descricao="Mouse RGB",
                  codigo_barra="123456789",
                  preco_custo=50.0,
                  vendivel=True,
                  preco_venda=100.0,
                  categoria="Periféricos")

produto2 = Produto(nome="Teclado Gamer",
                   descricao="Teclado RGB",
                   codigo_barra="987654321",
                   preco_custo=70.0,
                   vendivel=True,
                   preco_venda=120.0,
                   categoria="Periféricos")

produto3 = Produto(
    nome="Monitor Full HD 24",
    descricao="Monitor LED 24 polegadas Full HD",
    codigo_barra="7891234567890",
    preco_custo=450.0,
    vendivel=True,
    preco_venda=799.90,
    categoria="Monitores"
)

produto4 = Produto(
    nome="Mouse Sem Fio",
    descricao="Mouse óptico sem fio 1600 DPI",
    codigo_barra="7894561237890",
    preco_custo=35.0,
    vendivel=True,
    preco_venda=59.90,
    categoria="Periféricos"
)

# repo = ProdutoRepository("banco.sqlite")
id = 1
nome = 'Luca'

# repo.salvar(produto)
# repo.salvar(produto2)
# repo.salvar(produto3)
# repo.salvar(produto4)
# repo.atualizar(produto3, 3)
# repo.deletar(4)
array = ('id', 'nome', 'descricao', 'preco_custo', 'preco_venda')
# print(repo.listar(array))
# print(repo.buscar_por_id(array, 1))

#produto_service = ProdutoService()
#produto_service.cadastrar_produto(produto)
#produto_service.cadastrar_produto(produto2)
#print(produto_service.listar_produto(['id', 'nome', 'preco_venda']))
#produto_repository = ProdutoRepository('estoque.sqlite')

usuario = Usuario('Administrador')

fornecedor = Fornecedor(
        nome="Fornecedor Teste",
        cpf_cnpj="11444777000161",
        email="fornecedor@email.com",
        telefone="69999999999",
        endereco="Rua Teste",
        cidade="Porto Velho",
        estado="RO"
    )

movimentacao_entrada = Movimentacao(
        produto=produto,
        fornecedor=fornecedor,
        tipo=TipoMovimentacao.ENTRADA,
        quantidade=20,
        observacao="Reposição de estoque",
        usuario=usuario
    )
# print(movimentacao_entrada)
produto_service = ProdutoService()
fornecedor_service = FornecedorService()
usuario_service = UsuarioService()
estoque_service = EstoqueService()
movimentacao_service = MovimentacaoService()

produto_teste = Produto(
    nome="Mouse Gamer",
    descricao="Mouse RGB",
    codigo_barra="123456789",
    preco_custo=50.0,
    vendivel=True,
    preco_venda=150.0,
    categoria="Periféricos"
)

""" print(f"produto: {produto_service.listar_produto()}")
print(f"fornecedor: {fornecedor_service.listar_fornecedor()}")
print(f"usuario: {usuario_service.listar_usuario()}")
print(f"estoque: {estoque_service.listar_estoque()}")
print(f"movimentação: {movimentacao_service.listar_movimentacao()}") """

""" print(f"produto: {produto_service.buscar_produto(1)}")
print(f"fornecedor: {fornecedor_service.buscar_fornecedor(1)}")
print(f"usuario: {usuario_service.buscar_usuario(1)}")
print(f"estoque: {estoque_service.buscar_estoque(1)}")
print(f"movimentação: {movimentacao_service.buscar_movimentacao(1)}") """
produto_service.atualizar_produto(produto_teste, 1)
print(f"produto: {produto_service.listar_produto()}")