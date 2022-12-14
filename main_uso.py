#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto

pessoa1 = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
print(pessoa1)


end1 = Endereco('08320330', 430)
print(end1)

end2 = Endereco('04546042', 300)
print(end2)

pessoa1.adicionar_endereco('casa', end1)

pessoa1.listar_enderecos()

pessoa1.adicionar_endereco('trabalho', end2)

pessoa1.listar_enderecos()