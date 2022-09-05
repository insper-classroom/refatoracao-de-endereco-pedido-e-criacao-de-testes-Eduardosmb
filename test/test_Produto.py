import pytest
from classes.Produto import Produto


@pytest.mark.produto
def test_novo_id():
    p = Produto('0010342967')
    p.set_id(3)
    assert p.get_id() == 3

@pytest.mark.produto
def test_to_dict():
    p = Produto("0010342967", "Sabonete")
    assert p.to_dict() == {'id': "0010342967", 'nome': "Sabonete"}

