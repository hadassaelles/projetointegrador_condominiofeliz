def is_sindico(user):
    return user.is_superuser or user.groups.filter(name='Sindico').exists()

def is_funcionario(user):
    return user.is_superuser or user.groups.filter(name__in=['Sindico', 'Funcionario']).exists()