from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from pessoas.models import Pessoa, Morador, Sindico, Funcionario, Telefone
from apartamentos.models import Apartamento
from reservas.models import Area
from mensagens.models import Comunicado, Ocorrencia


class Command(BaseCommand):
    help = 'Popula o banco de dados com usuários, perfis, apartamentos e dados iniciais de teste.'

    def handle(self, *args, **options):
        senha_padrao = 'condominio123'
        self.stdout.write(self.style.NOTICE('Iniciando o povoamento do banco de dados...'))

        # 1. Grupos
        grupo_sindico, _ = Group.objects.get_or_create(name='Sindico')
        grupo_funcionario, _ = Group.objects.get_or_create(name='Funcionario')
        grupo_morador, _ = Group.objects.get_or_create(name='Morador')

        # 2. Apartamentos
        apto_101, _ = Apartamento.objects.get_or_create(numero='101')
        apto_102, _ = Apartamento.objects.get_or_create(numero='102')
        apto_201, _ = Apartamento.objects.get_or_create(numero='201')

        # 3. Áreas Comuns para Reservas
        area_churrasqueira, _ = Area.objects.get_or_create(
            nome='Churrasqueira Gourmet',
            defaults={'icone': '🍖', 'capacidade': 25}
        )
        area_salao, _ = Area.objects.get_or_create(
            nome='Salão de Festas',
            defaults={'icone': '🎉', 'capacidade': 60}
        )
        area_piscina, _ = Area.objects.get_or_create(
            nome='Espaço Piscina / Deck',
            defaults={'icone': '🏊', 'capacidade': 30}
        )

        # 4. Usuário: SÍNDICO
        user_sindico, created = User.objects.get_or_create(
            username='sindico',
            defaults={
                'first_name': 'Carlos',
                'last_name': 'Administrador',
                'email': 'sindico@condominiofeliz.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        user_sindico.set_password(senha_padrao)
        user_sindico.is_staff = True
        user_sindico.is_superuser = True
        user_sindico.save()
        user_sindico.groups.add(grupo_sindico)

        # Perfil Sindico (Pessoa)
        sindico_profile = Sindico.objects.filter(user=user_sindico).first()
        if not sindico_profile:
            sindico_profile = Sindico.objects.create(
                user=user_sindico,
                nome='Carlos',
                sobrenome='Administrador',
                cpf='111.111.111-11',
                email='sindico@condominiofeliz.com',
            )

        # 5. Usuário: FUNCIONÁRIO
        user_funcionario, created = User.objects.get_or_create(
            username='funcionario',
            defaults={
                'first_name': 'Marcos',
                'last_name': 'Porteiro',
                'email': 'funcionario@condominiofeliz.com',
                'is_staff': True,
            }
        )
        user_funcionario.set_password(senha_padrao)
        user_funcionario.is_staff = True
        user_funcionario.save()
        user_funcionario.groups.add(grupo_funcionario)

        # Perfil Funcionario (Pessoa)
        func_profile = Funcionario.objects.filter(user=user_funcionario).first()
        if not func_profile:
            func_profile = Funcionario.objects.create(
                user=user_funcionario,
                nome='Marcos',
                sobrenome='Porteiro',
                cpf='222.222.222-22',
                email='funcionario@condominiofeliz.com',
                cargo='Portaria e Segurança',
                sindico_responsavel=sindico_profile,
            )

        # 6. Usuário: MORADOR
        user_morador, created = User.objects.get_or_create(
            username='morador',
            defaults={
                'first_name': 'Hadassa',
                'last_name': 'Elles',
                'email': 'morador@condominiofeliz.com',
            }
        )
        user_morador.set_password(senha_padrao)
        user_morador.save()
        user_morador.groups.add(grupo_morador)

        # Perfil Morador (Pessoa)
        morador_profile = Morador.objects.filter(user=user_morador).first()
        if not morador_profile:
            morador_profile = Morador.objects.create(
                user=user_morador,
                nome='Hadassa',
                sobrenome='Elles',
                cpf='333.333.333-33',
                email='morador@condominiofeliz.com',
                apartamento=apto_101,
            )
        else:
            morador_profile.apartamento = apto_101
            morador_profile.save()

        # Vincula proprietário do apto 101 ao morador
        apto_101.proprietario = morador_profile
        apto_101.sindico = sindico_profile
        apto_101.save()

        # Telefones de exemplo
        Telefone.objects.get_or_create(
            pessoa=morador_profile,
            tipo='Celular',
            defaults={'numero': '(11) 98765-4321'}
        )
        Telefone.objects.get_or_create(
            pessoa=func_profile,
            tipo='Portaria',
            defaults={'numero': '(11) 91234-5678'}
        )

        # 7. Dados de demonstração (Comunicado inicial e Ocorrência inicial)
        Comunicado.objects.get_or_create(
            titulo='Bem-vindos ao Condomínio Feliz!',
            defaults={
                'conteudo': 'Prezados moradores, o sistema de gestão do condomínio está no ar para agendamento de áreas comuns, comunicados e ocorrências.',
                'autor': user_sindico,
            }
        )

        Ocorrencia.objects.get_or_create(
            titulo='Lâmpada do hall de entrada queimada',
            defaults={
                'morador': morador_profile,
                'categoria': Ocorrencia.Categoria.MANUTENCAO,
                'descricao': 'A lâmpada principal do hall próximo aos elevadores está piscando e precisa de substituição.',
                'unidade': 'Apto 101',
                'status': Ocorrencia.Status.ABERTA,
            }
        )

        self.stdout.write(self.style.SUCCESS(''))
        self.stdout.write(self.style.SUCCESS('====================================================='))
        self.stdout.write(self.style.SUCCESS('   ✔ BANCO DE DADOS POPULADO COM SUCESSO!'))
        self.stdout.write(self.style.SUCCESS('====================================================='))
        self.stdout.write(self.style.WARNING(f' Senha para todas as contas: {senha_padrao}'))
        self.stdout.write(self.style.SUCCESS('-----------------------------------------------------'))
        self.stdout.write(self.style.SUCCESS(' [SÍNDICO]'))
        self.stdout.write(f'   Usuário: sindico')
        self.stdout.write(f'   Acesso:  Painel do Síndico + Django Admin')
        self.stdout.write(self.style.SUCCESS('-----------------------------------------------------'))
        self.stdout.write(self.style.SUCCESS(' [FUNCIONÁRIO / PORTARIA]'))
        self.stdout.write(f'   Usuário: funcionario')
        self.stdout.write(f'   Acesso:  Painel do Funcionário (Reservas do dia / Encomendas)')
        self.stdout.write(self.style.SUCCESS('-----------------------------------------------------'))
        self.stdout.write(self.style.SUCCESS(' [MORADOR]'))
        self.stdout.write(f'   Usuário: morador')
        self.stdout.write(f'   Acesso:  Dashboard Morador (Apto 101, Ocorrências, Reservas)')
        self.stdout.write(self.style.SUCCESS('=====================================================' + '\n'))

