import pytest
from classes.Pedido import Pedido
from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica

# Carlos; 524.222.452-6; tiago@email.com, None, SP, Rua Clemente Falcão 430,

@pytest.mark.pedidos
def test_pedidos():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    end = Endereco('08320330', 430)
    pedido = Pedido(pessoa, end)
    assert pedido.__str__() == 'Carlos; 524.222.452-6; tiago@email.com, None, SP, Rua Clemente Falcão 430, '
    
@pytest.mark.pedidos
def test_status_pago():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    end = Endereco('08320330', 430)
    pedido = Pedido(pessoa, end) 
    pedido.status = Pedido.PAGO
    assert pedido.status == 2