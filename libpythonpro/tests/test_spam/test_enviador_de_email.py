import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['pedroh.af@hotmail.com', 'pedro.af200@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        remetente,
        'necromancerdoidao@outlook.com',
        'pytools',
        'teste do TDD pytools'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'pedro']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'necromancerdoidao@outlook.com',
            'pytools',
            'teste do TDD pytools'
    )




