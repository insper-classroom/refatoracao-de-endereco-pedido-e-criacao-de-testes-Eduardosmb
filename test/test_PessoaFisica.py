import pytest
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

end = Endereco('08320330', 430)

@pytest.mark.PessoaFisica
def test_adicionar_endereco():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    pessoa.adicionar_endereco('casa', end)
    assert pessoa.listar_enderecos() == ['casa']

@pytest.mark.PessoaFisica
def test_remover_endereco():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    pessoa.adicionar_endereco('casa', end)
    pessoa.remover_endereco

@pytest.mark.PessoaFisica
def test_busca_nome_pessoa():
    PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    assert PessoaFisica.busca_nome('Carlos') == ['Carlos']



