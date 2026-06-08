#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : fornecedor.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 06/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from validacao_cpf_cnpj import Validadora


class Fornecedor:
    def __init__(self, nome: str, cpf_cnpj: str,
                 email: str, telefone: str,
                 endereco: str,
                 cidade: str, estado: str,
                 id: int | None = None):

        self._nome = nome
        Validadora().validar_documento(cpf_cnpj)
        self._cpf_cnpj = cpf_cnpj
        self._email = email
        self._telefone = telefone
        self._endereco = endereco
        self._cidade = cidade
        self._estado = estado
        self._id = id

        campos = [nome,
                  email,
                  telefone,
                  endereco,
                  cidade,
                  estado]

        if any(not campo.strip() for campo in campos):
            raise ValueError("""Todos os campos
                            devem ser preechidos.""")

    def __str__(self):
        return (
            f"""Fornecedor(
            nome: {self.nome}
            cpf_cnpj: {self.cpf_cnpj}
            email: {self.email}
            telefone: {self.telefone}
            endereço: {self.endereco}
            cidade: {self.cidade}
            estado: {self.estado}
            )"""
        )

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf_cnpj(self) -> str:
        return self._cpf_cnpj

    @property
    def email(self) -> str:
        return self._email

    def alterar_email(self, novo_email: str):
        self._verifica_se_string_esta_vazia(novo_email)
        self._email = novo_email

    @property
    def telefone(self) -> str:
        return self._telefone

    def alterar_telefone(self, novo_telefone: str):
        self._verifica_se_string_esta_vazia(novo_telefone)
        self._telefone = novo_telefone

    @property
    def endereco(self) -> str:
        return self._endereco

    def alterar_endereco(self, novo_endereco: str):
        self._verifica_se_string_esta_vazia(novo_endereco)
        self._endereco = novo_endereco

    @property
    def cidade(self) -> str:
        return self._cidade

    def alterar_cidade(self, nova_cidade: str):
        self._verifica_se_string_esta_vazia(nova_cidade)
        self._cidade = nova_cidade

    @property
    def estado(self) -> str:
        return self._estado

    def alterar_estado(self, novo_estado: str):
        self._verifica_se_string_esta_vazia(novo_estado)
        self._estado = novo_estado

    def _verifica_se_string_esta_vazia(self, string: str):
        if not string.strip():
            raise ValueError("Campo vazio.")
