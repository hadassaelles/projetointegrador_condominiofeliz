import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.db import transaction

from apartamentos.models import Apartamento

from mensagens.models import Comunicado, Ocorrencia
from pessoas.models import Pessoa, Morador, Sindico, Funcionario


class Command(BaseCommand):
    help = "Cria usuários e dados iniciais (seed) para o projeto."

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            self._create_groups()
            self._create_users()
            self._create_apartamento()
            self._create_areas()
            self._create_demo_contents()
            self.stdout.write(self.style.SUCCESS(
                "\n✅ Seed concluído com sucesso!\nUsuários criados (senha: 'condominio123'):\n  • sindico\n  • funcionario\n  • morador\n"))
        except Exception as exc:
            self.stderr.write(self.style.ERROR(f"❌ Erro ao executar o seed: {exc}"))
            sys.exit(1)

    def _get_or_create_group(self, name):
        group, _ = Group.objects.get_or_create(name=name)
        return group

    def _create_groups(self):
        for name in ["Sindico", "Funcionario", "Morador"]:
            self._get_or_create_group(name)

    def _create_user(self, username, group_name, is_staff=False, is_superuser=False):
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"is_staff": is_staff, "is_superuser": is_superuser},
        )
        if created:
            user.set_password("condominio123")
            user.save()
            self.stdout.write(f"  • Usuário '{username}' criado.")
        else:
            self.stdout.write(f"  • Usuário '{username}' já existia.")
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        return user

    def _create_users(self):
        # síndico – staff + superuser
        self._create_user("sindico", "Sindico", is_staff=True, is_superuser=True)
        # funcionário – staff
        self._create_user("funcionario", "Funcionario", is_staff=True)
        # morador – usuário comum
        self._create_user("morador", "Morador")
        self._ensure_profiles()

    def _ensure_profiles(self):
        user = User.objects.get(username="sindico")
        if not Sindico.objects.filter(user=user).exists():
            Sindico.objects.create(user=user, nome="Síndico Demo")
            self.stdout.write("  • Perfil Sindico criado.")
        else:
            self.stdout.write("  • Perfil Sindico já existia.")

        user = User.objects.get(username="funcionario")
        if not Funcionario.objects.filter(user=user).exists():
            Funcionario.objects.create(user=user, nome="Funcionário Demo")
            self.stdout.write("  • Perfil Funcionario criado.")
        else:
            self.stdout.write("  • Perfil Funcionario já existia.")

        user = User.objects.get(username="morador")
        if not Morador.objects.filter(user=user).exists():
            mor = Morador.objects.create(user=user, nome="Morador Demo")
            self.stdout.write("  • Perfil Morador criado.")
        else:
            mor = Morador.objects.get(user=user)
            self.stdout.write("  • Perfil Morador já existia.")
        self.morador = mor

    def _create_apartamento(self):
        apt, created = Apartamento.objects.get_or_create(
            numero=101,
            defaults={"bloco": "A", "valor_condominio": 500},
        )
        if created:
            self.stdout.write("  • Apartamento 101 criado.")
        else:
            self.stdout.write("  • Apartamento 101 já existia.")
        sindico = Sindico.objects.get(user__username="sindico")
        apt.sindico = sindico
        apt.save()
        self.morador.apartamento = apt
        self.morador.save()

    def _create_areas(self):
        for name in ["Churrasqueira", "Salão", "Piscina"]:
            area, created = Area.objects.get_or_create(nome=name)
            if created:
                self.stdout.write(f"  • Área '{name}' criada.")
            else:
                self.stdout.write(f"  • Área '{name}' já existia.")

    def _create_demo_contents(self):
        if not Comunicado.objects.filter(titulo="Comunicação de Teste").exists():
            Comunicado.objects.create(
                titulo="Comunicação de Teste",
                conteudo="Este é um comunicado de demonstração.",
                autor=Sindico.objects.get(user__username="sindico"),
            )
            self.stdout.write("  • Comunicado de teste criado.")
        else:
            self.stdout.write("  • Comunicado de teste já existia.")

        if not Ocorrencia.objects.filter(titulo="Ocorrência de Teste").exists():
            Ocorrencia.objects.create(
                titulo="Ocorrência de Teste",
                descricao="Descrição da ocorrência de demonstração.",
                responsavel=self.morador,
                categoria="GERAL",
            )
            self.stdout.write("  • Ocorrência de teste criada.")
        else:
            self.stdout.write("  • Ocorrência de teste já existia.")

