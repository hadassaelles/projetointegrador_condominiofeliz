def _get_pessoa(user):
    return getattr(user, 'pessoa', None)


def is_sindico(user):
    if user.is_superuser:
        return True
    pessoa = _get_pessoa(user)
    return bool(pessoa and hasattr(pessoa, 'sindico'))


def is_funcionario(user):
    if user.is_superuser:
        return True
    pessoa = _get_pessoa(user)
    if not pessoa:
        return False
    return hasattr(pessoa, 'sindico') or hasattr(pessoa, 'funcionario')


def get_morador(user):
    """Retorna o Morador do usuário logado, ou None se ele não for morador."""
    pessoa = _get_pessoa(user)
    if pessoa and hasattr(pessoa, 'morador'):
        return pessoa.morador
    return None