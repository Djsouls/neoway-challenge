from neoway.models import CPFModel, CNPJModel

def test_cpf_mode_creation():
    """Testa a crição de um cpf a partir do nosso modelo"""

    cpf_text = '12345678910'

    cpf = CPFModel(cpf=cpf_text)

    assert cpf.cpf == cpf_text

def test_cnpj_mode_creation():
    """Testa a crição de um cnpj a partir do nosso modelo"""

    cnpj_text = '73123394000149'

    cnpj = CNPJModel(cnpj=cnpj_text)

    assert cnpj.cnpj == cnpj_text
