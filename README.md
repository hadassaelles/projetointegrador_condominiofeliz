# TRABALHO DE PI: Condomínio Feliz
Trabalho desenvolvido durante a disciplina de Projeto Integrador

### 1. COMPONENTES
- Ana Beatriz Soares - anabeeas12@gmail.com  
- Ana Clara Vianna - anaclaravianna2005@gmail.com  
- Arthur de Oliveira Matias dos Santos - ao451427@gmail.com  
- Hadassa Daulani Elles - hadaulles@gmail.com  
- Isabelly Rodrigues Neves - isa.secund07@gmail.com  
- Pietro de Oliveira Mantovani - mantovanipietro05@gmail.com  

---

### 2. Ideias Selecionadas, Matriz de Seleção e Opportunity Card

#### 2.1 Ideias geradas pelo grupo (uma por integrante)

Após a Dinâmica Prática 5-5-5, cada membro do grupo apresentou uma ideia:

- **Ana Beatriz**: Aplicativo de controle de gastos compartilhados entre amigos e roommates  
- **Ana Clara**: Sistema de agendamento e organização de grupos de estudo  
- **Arthur**: Rede social para donos de cachorros  
- **Hadassa**: Sistema de gestão de condomínio  
- **Isabelly**: Plataforma de empréstimo e troca de materiais escolares entre alunos  
- **Pietro**: Aplicativo de caronas solidárias entre estudantes  

#### 2.2 Matriz de Seleção (critérios oficiais – 0 a 2 pontos cada | máximo 10 pontos)

| Critério                              | Ana Beatriz<br>Gastos Compartilhados | Ana Clara<br>Grupos de Estudo | Arthur<br>Rede Social Cachorros | **Hadassa**<br>**Sistema de Condomínio** | Isabelly<br>Empréstimo Materiais | Pietro<br>Caronas Solidárias |
|---------------------------------------|--------------------------------------|-------------------------------|----------------------------------|------------------------------------------|----------------------------------|------------------------------|
| **Afinidade** (quero trabalhar nisso?) | 1                                    | 2                             | 1                                | **2**                                    | 1                                | 2                            |
| **Acesso** (consigo falar com usuários?) | 2                                  | 2                             | 1                                | **2**                                    | 2                                | 2                            |
| **Problema** (incomoda alguém de fato?) | 1                                   | 1                             | 1                                | **2**                                    | 1                                | 1                            |
| **Software** (software gera valor real?) | 2                                  | 2                             | 1                                | **2**                                    | 1                                | 1                            |
| **Viabilidade** (dá para MVP em ~60h?) | 2                                   | 2                             | 1                                | **2**                                    | 1                                | 1                            |
| **Nota Final**                        | **8**                                | **9**                         | **5**                            | **10**                                   | **6**                            | **7**                        |

**Resultado da Seleção**  
A ideia escolhida pelo grupo foi a da **Hadassa – Sistema de Gestão de Condomínio**, que obteve a pontuação máxima (**10 pontos**).

**Justificativa da escolha:**
- Maior afinidade do grupo com o tema (proposta original da Hadassa e identificação coletiva).
- Fácil acesso a usuários reais (síndico conhecido + colegas do curso que moram em condomínio).
- Problema real e recorrente: gestão desorganizada via WhatsApp e planilhas.
- Software gera valor claro e mensurável para síndicos e moradores.
- Alta viabilidade para desenvolver um MVP no tempo da disciplina.

#### 2.3 Opportunity Card da ideia selecionada

1. **Área de afinidade/contexto**  
   Gestão de condomínios residenciais (pequenos e médios). Interesse do grupo em resolver problemas reais do dia a dia de síndicos e moradores.

2. **Problema percebido**  
   Dificuldade de gerenciar demandas do condomínio de forma organizada (ocorrências, reservas de áreas comuns, visitantes e comunicados). Tudo acaba sendo feito de forma improvisada.

3. **Quem possui o problema**  
   Síndicos (principalmente de condomínios pequenos e médios) e, em segundo plano, os moradores.

4. **Como é resolvido hoje**  
   Planilhas no Excel + grupos de WhatsApp. Algumas vezes cadernos ou anotações manuais. Não existe histórico confiável nem controle de status.

5. **Soluções semelhantes**  
   Softwares profissionais de gestão condominial (ex: Superlógica, Condor, TownSq). São caros, complexos e pouco acessíveis para condomínios menores.

6. **Lacuna inicial**  
   Falta de uma solução simples, barata (ou gratuita no início) e fácil de usar, focada especificamente em condomínios pequenos/médios, com versão mobile + web.

7. **Pessoas acessíveis**  
   - 1 síndico conhecido  
   - Colegas do curso que moram em condomínio  
   - Possibilidade de conversar com porteiros e moradores

8. **Hipótese de oportunidade**  
   “Acreditamos que síndicos de condomínios pequenos e médios perdem tempo significativo e sofrem com falhas de comunicação ao gerenciar ocorrências, reservas e visitantes apenas com WhatsApp e planilhas. Precisamos investigar se uma solução digital simples seria adotada e se resolve de fato a dor.”

9. **Fomento/oportunidade**  
   Nenhum edital específico identificado no momento.  
   *(Justificativa: projeto acadêmico. Caso surja oportunidade de fomento depois, será avaliado.)*

10. **Principal incerteza/desafio**  
    - Validar se os síndicos realmente sentem a dor com intensidade suficiente  
    - Conseguir engajamento dos usuários para testar o MVP  
    - Limitação de tempo da equipe para desenvolver funcionalidades mais complexas

---

### 3. MINIMUNDO

Um condomínio possui um ou mais blocos, e cada bloco possui diversas unidades (apartamentos ou casas), identificadas por número e vinculadas a um único bloco. Cada unidade tem um proprietário responsável e pode ter um ou mais moradores (podendo o proprietário ser um deles), com nome, CPF, telefone, e-mail e data de nascimento.

O condomínio possui funcionários (manutenção, limpeza, portaria, administração), com matrícula, cargo, telefone e email.

Moradores podem registrar ocorrências (manutenção, reclamações, sugestões ou denúncias), com data de abertura, descrição, categoria, status (aberta, em andamento ou concluída) e um funcionário responsável pelo atendimento.

Há áreas comuns (salão de festas, churrasqueira, academia, piscina, quadra) reserváveis pelos moradores, com data, horário de início/término e status (confirmada, cancelada ou concluída).

Mensalmente são geradas taxas condominiais por unidade, com valor, vencimento, data de pagamento, status (paga/pendente) e possíveis multas ou juros por atraso.

A administração envia comunicados aos moradores, com título, descrição, data de publicação e destino (todos ou um bloco específico).

O sistema também controla visitantes, registrando nome, documento, horários de entrada/saída e unidade visitada, podendo a entrada ser autorizada previamente por um morador.

Por fim, o administrador tem acesso completo, cadastrando moradores, funcionários, unidades, áreas comuns, reservas, ocorrências e comunicados, além de acompanhar os pagamentos das taxas.

---

### 4. Validação da Ideia

a) Link do formulário desenvolvido:  
https://forms.gle/xhYWbRj1YiUC2JkR9  

b) Link para Relatório/Apresentação de resultados obtidos:  
[Apresentação do formulário.pptx](https://github.com/user-attachments/files/31534415/Apresentacao.do.formulario.pptx)

---

### 4.1 Digital Investigation Card

**O que aprendemos com o público?**  
**O que aprendemos que não sabíamos antes de entrevistar o público-alvo?**

<img width="1376" height="752" alt="WhatsApp Image 2026-09-25 at 19 49 45" src="https://github.com/user-attachments/assets/1c37675f-4909-47b7-aa61-f2d83e58ec8e" />


**Pitch das Evidências:**  
Realizamos pesquisa via Google Forms com 2 alunos do IFES que têm experiência em condomínios. Identificamos dificuldade de gerenciamento e acesso a informações.  
**Principal descoberta:** usuários têm dificuldade em localizar e organizar informações de forma rápida e clara.  
**Descoberta inesperada:** o tamanho dos botões impacta a usabilidade.  
**Dúvida restante:** como a solução se comportará em condomínios de portes diferentes.

---

### 5. Personas e Histórias de Usuário

#### 5.1 Personas


[personas.pdf](https://github.com/user-attachments/files/32672313/personas.pdf)


**Persona 1 – Maria, 40 anos (Moradora)**  
- Moradora do condomínio  
- Especialidade: participação na comunidade  
- Foco: comunicação e interação entre moradores  
- Avalia o sistema por: app de fácil acesso, comunicados sempre atualizados, administração eficiente  
- Pontos de atenção: interface simples e maior fluidez ao navegar  
- Não quer: app complexo e muitas informações irrelevantes  

**Persona 2 – Ricardo, 53 anos (Síndico)**  
- Síndico do condomínio  
- Especialidade: gestão e administração  
- Foco: manter o condomínio organizado e seguro  
- Avalia o sistema por: facilidade em administrar o app e organizar reservas  
- Pontos de atenção: eficácia e facilidade em administrar o condomínio  
- Não quer: dificuldade em entender a interface  

**Persona 3 – Paulo, 34 anos (Funcionário)**  
- Funcionário do condomínio (manutenção)  
- Especialidade: manutenção e conservação  
- Foco: organização e segurança  
- Avalia o sistema por: praticidade e organização das informações e ocorrências  
- Pontos de atenção: fluidez ao navegar e receber avisos rapidamente  
- Não quer: app complexo e funcionalidades desnecessárias  

#### 5.2 Histórias de Usuário

- Como **morador**, eu quero praticidade em receber os comunicados do condomínio para me manter informado sobre os eventos e mudanças importantes.  
- Como **síndico**, eu quero facilidade em administrar o condomínio para divulgar os comunicados.  
- Como **funcionário**, eu quero eficiência em receber as tarefas do dia para organizar minha rotina.  
- Como **morador**, eu quero registrar ocorrências pelo aplicativo para informar problemas de forma rápida e eficaz.  
- Como **síndico**, eu quero gerenciar as reservas das áreas de lazer e dos visitantes para evitar conflitos de horários.  
- Como **funcionário**, eu quero enviar atualizações sobre os serviços realizados para facilitar o acompanhamento pelo síndico.

---

### 6. PROTÓTIPOS DO SISTEMA


[prototipo.pdf](https://github.com/user-attachments/files/32672323/prototipo.pdf)


O protótipo do sistema (versão web) está disponível no arquivo:  
**prototipo.pdf**

Principais telas desenvolvidas (visão do Síndico/Administrador):
- Login com seleção de perfil (Administrador, Morador, Funcionário/Portaria)
- Dashboard com resumo (ocorrências abertas, moradores, reservas, comunicados)
- Gestão de Blocos e Unidades
- Gestão de Moradores
- Gestão de Funcionários
- Gestão de Ocorrências
- Gestão de Reservas de Áreas Comuns
- Gestão de Comunicados
- Controle de Visitantes

---

### 7. MODELO CONCEITUAL


<img width="808" height="622" alt="WhatsApp Image 2026-09-25 at 19 57 10" src="https://github.com/user-attachments/assets/d67900f7-c8b3-4ff6-9ef9-69e04d9ea7fd" />


O modelo conceitual foi desenvolvido utilizando a notação Entidade-Relacionamento (BR Modelo).

**Principais entidades:**
- Pessoa (especialização: Morador, Síndico, Funcionário)
- Apartamento
- Reserva
- Convidados
- Encomenda
- Mensagem
- Telefone

*(Inserir aqui a imagem do Modelo Conceitual)*

---

### 8. Descrição dos Dados

- **Pessoa**: Armazena os dados básicos das pessoas do sistema (nome, sobrenome, CPF, e-mail).  
- **Morador**: Especialização de Pessoa. Representa os moradores das unidades.  
- **Síndico**: Especialização de Pessoa. Representa o síndico responsável pela administração.  
- **Funcionário**: Especialização de Pessoa. Representa os funcionários do condomínio (com cargo).  
- **Apartamento**: Representa as unidades do condomínio (número, proprietário, síndico).  
- **Reserva**: Armazena as reservas de áreas comuns (data, tempo, local, quantidade de pessoas).  
- **Convidados**: Pessoas convidadas vinculadas a uma reserva.  
- **Encomenda**: Controle de encomendas recebidas no condomínio.  
- **Mensagem**: Comunicados e mensagens trocadas no sistema.  
- **Telefone**: Números de telefone vinculados às pessoas.

---

### 9. Rastreabilidade dos Artefatos

#### a) Histórias de Usuário × Protótipo

| História de Usuário                                      | Tela do Protótipo                  |
|----------------------------------------------------------|------------------------------------|
| Morador receber comunicados                              | Tela de Comunicados                |
| Síndico divulgar comunicados                             | Tela de Comunicados + Dashboard    |
| Funcionário receber tarefas do dia                       | Tela de Ocorrências / Dashboard    |
| Morador registrar ocorrências                            | Tela de Ocorrências                |
| Síndico gerenciar reservas e visitantes                  | Tela de Reservas + Visitantes      |
| Funcionário enviar atualizações de serviços              | Tela de Ocorrências                |

#### b) Protótipo × Modelo Conceitual

| Funcionalidade do Protótipo     | Entidades envolvidas              |
|--------------------------------|-------------------------------------|
| Gestão de Moradores            | Pessoa, Morador, Apartamento        |
| Gestão de Funcionários         | Pessoa, Funcionário                 |
| Gestão de Ocorrências          | (precisa ser melhor mapeada)        |
| Gestão de Reservas             | Reserva, Convidados, Apartamento    |
| Comunicados                    | Mensagem                            |
| Controle de Visitantes         | Convidados / Reserva                |

---

### 10. Project Model Canvas (GP)


<img width="1600" height="938" alt="WhatsApp Image 2026-09-25 at 20 22 13" src="https://github.com/user-attachments/assets/70d13ff1-3880-4551-8b03-faf3a76d91e3" />




**Resumo do Canvas:**

- **Justificativas**:  
  - Falta de comunicação entre gestão do condomínio, sindico e moradores gerando atrasos.  
  - Falta de canal direto com síndico e baixa transparência.

- **Produto**: Gestão de condomínio - Sistema Web com comunicados e demandas em tempo real

- **Stakeholders Externos**: Funcionários e moradores de condomínios residenciais, síndico e administração.

- **Premissas**: Disponibilidade de infraestrutura: internet, computadores e horários extraclasse dedicados ao desenvolvimento. Comunicação efetiva com moradores e equipe.

- **Riscos**: Prazo acadêmico apertado. Indisponibilidade eventual de computadores ou internet.

- **Objetivo SMART**: Reduzir em 40% o tempo de resolução de demandas em 3 meses, gerando eficiência e satisfação aos moradores através de informações centralizadas.

- **Requisitos**:  
  - Cadastrar novos moradores com perfis.  
  - Mostrar eventos importantes com notificações.  
  - Fazer agendamentos de áreas comuns.  
  - Fazer denúncias e reclamações com rastreamento.

- **Equipe**: Ana B., Arthur, Ana C., Hadassa | Isabelly e Pietro

- **Grupo de Entregas**:  
  1. Entrega das funções básicas do sistema para uso da ferramenta  
  2. Requisitos não funcionais, segurança e documentação

- **Benefícios Futuro**:  
  - Mais organização e segurança. Redução do tempo gasto em administração manual.  
  - Melhor comunicação e convívio entre condôminos.

- **Restrições**:  
  - Prazo curto definido pelo calendário acadêmico.  
  - Desenvolvimento limitado a horários extraclasse da equipe.

- **Custos**: R$ 1.560,00 - Projeto acadêmico: Hospedagem R$ 800,00, Domínio R$ 120,00, Ferramentas e testes R$ 640,00. Sem custos de mão de obra - fins didáticos.

---

### 11. Divisão de Atividades do Grupo

| Atividade                                      | Quem elaborou          | Horas planejadas | Horas gastas |
|------------------------------------------------|------------------------|------------------|--------------|
| Desenvolvedor back-end (agendamento)           | Pietro Mantovani       | 300h             |              |
| Desenvolvedor back-end (reclamações)           | Arthur Oliveira        | 300h             |              |
| Desenvolvedor back-end (mural de comunicados)  | Hadassa                | 300h             |              |
| Desenvolvedor front-end (tela de reclamação)   | Isabelly Neves         | 300h             |              |
| Desenvolvedor front-end (tela de agendamento)  | Ana Clara              | 300h             |              |
| Desenvolvedor front-end (tela de mural)        | Ana Beatriz            | 300h             |              |

---

**Observação:**  
Este documento consolida todos os artefatos desenvolvidos pelo grupo.
