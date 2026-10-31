const modal = document.getElementById('modalOcorrencia');
const btnAbrir = document.getElementById('btnAbrirOcorrencia');
const btnFechar = document.getElementById('btnFecharModal');
const btnCancelar = document.getElementById('btnCancelar');

if (modal) {
  // Abrir pelo botão "+ Abrir ocorrência"
  if (btnAbrir) btnAbrir.addEventListener('click', () => modal.showModal());

  // Fechar pelo "X" e pelo "Cancelar"
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

  // Reabrir sozinho se o formulário voltou com erro (o Django marca isso no HTML)
  if (modal.dataset.abrir === '1') modal.showModal();
}