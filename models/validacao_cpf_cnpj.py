#!/usr/bin/env python 
"""
-----------------------------------------------------
Program    : cpf.py
Description: Arquivo para validar o cpf.
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 06/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from validate_docbr import CPF, CNPJ
import re

class Validadora:
    def validar_documento(self, documento : str) -> Cpf | Cnpj:
        self.verifica_se_documento_esta_vazio(documento)
        return self.retira_caracteres_nao_numericos_do_documento(documento) 

    def verifica_se_documento_esta_vazio(self, documento : str):
        if not documento.strip():
            raise ValueError("Campo documento vazio")

    def retira_caracteres_nao_numericos_do_documento(self, documento : str) -> Cpf | Cnpj: 
        documento_limpo = re.sub(r'[^0-9]', '', documento)
        return self.verifica_se_eh_cpf_ou_cnpj(documento_limpo)
        
    def verifica_se_eh_cpf_ou_cnpj(self, documento : str) -> Cpf | Cnpj:
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Documento inválido.")


class Cpf:

    def __init__(self, num_cpf):
        self.validador_cpf = CPF()
        self.cpf_eh_valido(num_cpf)
        self._cpf = num_cpf

    def cpf_eh_valido(self, num_cpf):
        if self.validador_cpf.validate(num_cpf) == False:
            raise ValueError("CPF inválido!")
    
    def __str__(self):
        return self.format_cpf()
    
    def format_cpf(self):
        fatia_um = self._cpf[:3]
        fatia_dois = self._cpf[3:6]
        fatia_tres = self._cpf[6:9]
        fatia_quatro = self._cpf[9:]

        return(
                "{}.{}.{}-{}".format(
                    fatia_um,
                    fatia_dois,
                    fatia_tres,
                    fatia_quatro
                    )
                )
    
class Cnpj:

    def __init__(self, num_cnpj):
        self.validador_cnpj = CNPJ()
        self.cnpj_eh_valido(num_cnpj)
        self._cnpj = num_cnpj

    def cnpj_eh_valido(self, num_cnpj):
        if self.validador_cnpj.validate(num_cnpj) == False:
            raise ValueError("CNPJ inválido!")
    
    def __str__(self):
        return self.format_cnpj()
    
    def format_cnpj(self):
        fatia_um = self._cnpj[:2]
        fatia_dois = self._cnpj[2:5]
        fatia_tres = self._cnpj[5:8]
        fatia_quatro = self._cnpj[8:12]
        fatia_cinco = self._cnpj[12:]

        return(
                "{}.{}.{}/{}-{}".format(
                    fatia_um,
                    fatia_dois,
                    fatia_tres,
                    fatia_quatro,
                    fatia_cinco
                    )
                )
    

