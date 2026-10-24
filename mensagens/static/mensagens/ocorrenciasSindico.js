const modal = document.getElementById('modalGerenciar');
const form = document.getElementById('formGerenciar');

if (modal && form) {
  const titulo = document.getElementById('modalTitulo');
  const descricao = document.getElementById('modalDescricao');
  const boxImagem = document.getElementById('modalImagem');
  const linkImagem = document.getElementById('linkImagem');
  const selResponsavel = document.getElementById('selResponsavel');
  const selSituacao = document.getElementById('selSituacao');

  document.querySelectorAll('.btn-gerenciar').forEach((botao) => {
    botao.addEventListener('click', () => {
      form.action = botao.dataset.url;
      titulo.textContent = botao.dataset.titulo;
      descricao.textContent = botao.dataset.descricao;
      selResponsavel.value = botao.dataset.responsavel;
      selSituacao.value = botao.dataset.situacao;

      if (botao.dataset.imagem) {
        linkImagem.href = botao.dataset.imagem;
        boxImagem.hidden = false;
      } else {
        boxImagem.hidden = true;
      }
      modal.showModal();
    });
  });

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
}