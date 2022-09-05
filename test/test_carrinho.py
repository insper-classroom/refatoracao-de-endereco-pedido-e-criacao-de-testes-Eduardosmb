import pytest
from classes.Carrinho import Carrinho
from classes.Produto import Produto

produto = Produto('0010342967', 'mouse')

@pytest.mark.carrinho
def test_adicionar_item():
    carrinho = Carrinho
    carrinho.adicionar_item(produto,3)
    assert carrinho.__str__() == {'0010342967': 3} 


@pytest.mark.carrinho
def test_remover_item():
    produto = Produto('0010342967', 'mouse')
    carrinho = Carrinho
    carrinho.adicionar_item(produto,3)
    carrinho.remover_item(produto)
    assert carrinho.__str__() == {'0010342967': 2} 
