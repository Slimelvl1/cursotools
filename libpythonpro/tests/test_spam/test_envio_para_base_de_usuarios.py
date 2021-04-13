from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario



@pytest.mark.parametrize(
    'usuarios',
    [
        [
        Usuario(nome='Pedro', email='necromancerdoidao@outlook.com'),
        Usuario(nome='Silvio', email='jsilvio.f@hotmail.com')
        ],
        [
        Usuario(nome='Pedro', email='necromancerdoidao@outlook.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'necromancerdoidao@outlook.com',
        'Pytools',
        'teste do pytools'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Pedro', email='necromancerdoidao@outlook.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedroh.af@hotmail.com',
        'Pytools',
        'teste do pytools'
    )
    enviador.enviar.assert_called_once_with(
        'pedroh.af@hotmail.com',
        'necromancerdoidao@outlook.com',
        'Pytools',
        'teste do pytools'
    )

