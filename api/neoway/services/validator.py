from validate_docbr import BaseDoc, CPF, CNPJ

def validate_cpf(cpf: str):
    return CPF().validate(cpf)

def validate_cnpj(cnpj: str):
    return CNPJ().validate(cnpj)