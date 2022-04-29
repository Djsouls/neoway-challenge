from validate_docbr import CPF, CNPJ

from neoway.services.validator import validate_cpf, validate_cnpj

def test_valid_cpfs_validation():
    """
    Testa se o serviço de validação de CPF está validando corretamente CPFs válidos
    """
    valid_cpfs = [
      '44815973210',
      '61879327651',
      '71412375509',
      '88412943619',
    ]

    for valid in valid_cpfs:
        assert validate_cpf(valid)

def test_invalid_cpfs_validation():
    """
    Testa se o serviço de validação de CPF está validando corretamente CPFs inválidos
    """
    invalid_cpfs = [
      '',
      '12345678912',
      '98765432198',
      '02020202025',
      '88552200258',
    ]

    for invalid in invalid_cpfs:
        assert not validate_cpf(invalid)

def test_valid_cnpjs_validation():
    """
    Testa se o serviço de validação de CNPJ está validando corretamente CNPJs válidos
    """
    valid_cnpjs = [
      '65906875000100',
      '83219218000169',
      '39882114000148',
      '11429854000104',
    ]

    for valid in valid_cnpjs:
        assert validate_cnpj(valid)

def test_invalid_cnpjs_validation():
    """
    Testa se o serviço de validação de CNPJ está validando corretamente CNPJs inválidos
    """
    invalid_cnpjs = [
      '',
      '11111111111111',
      '15552202123156',
      '22222222222222',
      '33333333333333',
    ]

    for invalid in invalid_cnpjs:
        assert not validate_cnpj(invalid)