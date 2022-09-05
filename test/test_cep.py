import pytest
from classes.Endereco import Endereco
import requests

@pytest.mark.cep
def test_checar_cep_numero_residencia_construcao_objeto():
    cep = '08320330'
    numero = 430
    assert 'SP, Rua Clemente Falcão 430, ' == Endereco(cep, numero).__str__()
@pytest.mark.cep
def test_cep_int_string():
    cep = '4521000'
    numero = 430
    end1 = Endereco(cep, numero)
    cep = end1.cep
    assert True == isinstance(cep,(int,str))

@pytest.mark.cep
def test_cep_invalido_numero_digitos():
    cep = Endereco.consultar_cep('123456789')
    assert False == cep

@pytest.mark.cep
def test_cep_invalido():
    cep = Endereco.consultar_cep('9999999')
    assert False == cep

@pytest.mark.cep
@pytest.mark.conexao
def test_cep_sem_conexao():
    with pytest.raises(requests.exceptions.ConnectionError) as e:
        Endereco.consultar_cep('4521000')
    assert 'Connection' in str(e.value)

