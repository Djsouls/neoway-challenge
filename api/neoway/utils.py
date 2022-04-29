from typing import List

def remove_chars(text: str, unwanted_chars: List[str]):
    for unwanted_char in unwanted_chars:
        text = text.replace(unwanted_char, '')

    return text

def clean_cpf(cpf: str) -> str:
    return remove_chars(cpf, ['.', '-'])

def clean_cnpj(cnpj: str) -> str:
    return remove_chars(cnpj, ['.', '/', '-'])