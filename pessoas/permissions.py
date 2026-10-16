def is_sindico(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser or user.groups.filter(name='Sindico').exists():
        return True
    return hasattr(user, 'pessoa') and hasattr(user.pessoa, 'sindico')


def is_funcionario(user):
    if not user.is_authenticated:
        return False
    if user.is_superuser or user.groups.filter(name__in=['Sindico', 'Funcionario']).exists():
        return True
    if hasattr(user, 'pessoa'):
        return hasattr(user.pessoa, 'funcionario') or hasattr(user.pessoa, 'sindico')
    return False


def is_morador(user):
    if not user.is_authenticated:
        return False
    if user.groups.filter(name='Morador').exists():
        return True
    if hasattr(user, 'pessoa') and hasattr(user.pessoa, 'morador'):
        return True
    # Qualquer usuário autenticado comum que não seja síndico ou funcionário é tratado como morador
    return not (is_sindico(user) or is_funcionario(user))