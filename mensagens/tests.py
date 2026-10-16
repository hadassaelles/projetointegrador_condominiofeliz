from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from pessoas.models import Morador, Sindico
from apartamentos.models import Apartamento
from mensagens.models import Ocorrencia


class OcorrenciasFlowTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Cria apartamento
        self.apto = Apartamento.objects.create(numero='101')

        # Cria Morador (que já herda de Pessoa e cria o registro em Pessoa)
        self.user_morador = User.objects.create_user(
            username='morador1',
            password='senha123',
            first_name='Ana',
            last_name='Silva'
        )
        self.morador = Morador.objects.create(
            user=self.user_morador,
            nome='Ana',
            sobrenome='Silva',
            cpf='111.111.111-11',
            email='ana@condominio.local',
            apartamento=self.apto
        )

        # Cria Síndico (que já herda de Pessoa)
        self.user_sindico = User.objects.create_user(
            username='sindico1',
            password='senha123',
            first_name='Carlos',
            last_name='Gestor'
        )
        grupo_sindico, _ = Group.objects.get_or_create(name='Sindico')
        self.user_sindico.groups.add(grupo_sindico)

        self.sindico = Sindico.objects.create(
            user=self.user_sindico,
            nome='Carlos',
            sobrenome='Gestor',
            cpf='222.222.222-22',
            email='carlos@condominio.local'
        )

    def test_fluxo_completo_ocorrencia(self):
        # 1. Morador faz login
        login_sucesso = self.client.login(username='morador1', password='senha123')
        self.assertTrue(login_sucesso)

        # Redirecionamento após login
        resp_redirect = self.client.get(reverse('redirecionar_apos_login'))
        self.assertRedirects(resp_redirect, reverse('home_morador'))

        # 2. Morador acessa tela de ocorrências
        resp_lista = self.client.get(reverse('mensagens:minhas_ocorrencias'))
        self.assertEqual(resp_lista.status_code, 200)

        # 3. Morador cria nova ocorrência
        dados_ocorrencia = {
            'categoria': 'MANUTENCAO',
            'titulo': 'Vazamento na torneira do salão',
            'descricao': 'Torneira pingando continuamente há 2 dias.',
            'unidade': 'Apto 101',
        }
        resp_post = self.client.post(reverse('mensagens:nova_ocorrencia'), data=dados_ocorrencia)
        self.assertRedirects(resp_post, reverse('mensagens:minhas_ocorrencias'))

        # Verifica se foi gravada no banco
        self.assertEqual(Ocorrencia.objects.count(), 1)
        ocorrencia = Ocorrencia.objects.first()
        self.assertEqual(ocorrencia.titulo, 'Vazamento na torneira do salão')
        self.assertEqual(ocorrencia.status, Ocorrencia.Status.ABERTA)

        # 4. Ocorrência aparece na página do morador
        resp_lista_apos = self.client.get(reverse('mensagens:minhas_ocorrencias'))
        self.assertContains(resp_lista_apos, 'Vazamento na torneira do salão')

        # Morador faz logout
        self.client.logout()

        # 5. Morador NÃO pode acessar a área de gerência do síndico
        self.client.login(username='morador1', password='senha123')
        resp_bloqueio = self.client.get(reverse('mensagens:gerenciar_ocorrencias'))
        self.assertEqual(resp_bloqueio.status_code, 302)
        self.client.logout()

        # 6. Síndico faz login e acessa a gestão de ocorrências
        self.client.login(username='sindico1', password='senha123')
        resp_sindico = self.client.get(reverse('mensagens:gerenciar_ocorrencias'))
        self.assertEqual(resp_sindico.status_code, 200)
        self.assertContains(resp_sindico, 'Vazamento na torneira do salão')

        # 7. Síndico atualiza o status para EM_ANDAMENTO
        resp_status = self.client.post(
            reverse('mensagens:atualizar_status_ocorrencia', args=[ocorrencia.id_ocorrencia]),
            data={'status': 'EM_ANDAMENTO'}
        )
        self.assertRedirects(resp_status, reverse('mensagens:gerenciar_ocorrencias'))

        ocorrencia.refresh_from_db()
        self.assertEqual(ocorrencia.status, 'EM_ANDAMENTO')
        self.assertEqual(ocorrencia.responsavel.id, self.sindico.id)
