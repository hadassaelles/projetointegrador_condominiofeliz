const modal = document.getElementById('modalComunicado');
const form = document.getElementById('formComunicado');

if (modal && form) {
  const tituloModal = document.getElementById('tituloModal');
  const btnEnviar = document.getElementById('btnEnviar');
  const campos = {
    titulo: document.getElementById('id_titulo'),
    categoria: document.getElementById('id_categoria'),
    prioridade: document.getElementById('id_prioridade'),
    conteudo: document.getElementById('id_conteudo'),
  };

  function abrirNovo() {
    form.action = form.dataset.urlNovo;
    tituloModal.textContent = 'Criar Novo Comunicado';
    btnEnviar.textContent = 'Publicar comunicado';
    campos.titulo.value = '';
    campos.categoria.value = 'GERAL';
    campos.prioridade.value = 'NORMAL';
    campos.conteudo.value = '';
    modal.showModal();
  }

  function abrirEdicao(botao) {
    form.action = botao.dataset.url;
    tituloModal.textContent = 'Editar Comunicado';
    btnEnviar.textContent = 'Salvar alterações';
    campos.titulo.value = botao.dataset.titulo;
    campos.categoria.value = botao.dataset.categoria;
    campos.prioridade.value = botao.dataset.prioridade;
    campos.conteudo.value = botao.dataset.conteudo;
    modal.showModal();
  }

  const btnNovo = document.getElementById('btnNovoComunicado');
  if (btnNovo) btnNovo.addEventListener('click', abrirNovo);

  document.querySelectorAll('.btn-editar').forEach((botao) => {
    botao.addEventListener('click', () => abrirEdicao(botao));
  });

  // Confirmação antes de excluir
  document.querySelectorAll('.form-excluir').forEach((f) => {
    f.addEventListener('submit', (e) => {
      if (!confirm('Excluir este comunicado? Essa ação não pode ser desfeita.')) e.preventDefault();
    });
  });

  // Fechar pelo "X" e pelo "Cancelar"
  const btnFechar = document.getElementById('btnFecharModal');
  const btnCancelar = document.getElementById('btnCancelar');
  if (btnFechar) btnFechar.addEventListener('click', () => modal.close());
  if (btnCancelar) btnCancelar.addEventListener('click', () => modal.close());

  // Fechar ao clicar fora (ignora cliques na margem interna do modal)
  modal.addEventListener('click', (e) => {
    if (e.target !== modal) return;
    const r = modal.getBoundingClientRect();
    const fora = e.clientX < r.left || e.clientX > r.right ||
                 e.clientY < r.top || e.clientY > r.bottom;
    if (fora) modal.close();
  });

  // Reabrir se o formulário voltou com erro
  if (modal.dataset.abrir === '1') modal.showModal();
}