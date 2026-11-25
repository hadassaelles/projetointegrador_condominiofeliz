const modal = document.getElementById('modalOcorrencia');
  const btnAbrir = document.getElementById('btnAbrirOcorrencia');
  const btnFechar = document.getElementById('btnFecharModal');
  const btnCancelar = document.getElementById('btnCancelar');

  // Abrir o modal
  btnAbrir.addEventListener('click', () => {
    modal.showModal();
  });

  // Fechar o modal
  btnFechar.addEventListener('click', () => {
    modal.close();
  });

  // Fechar o modal ao clicar no botão "Cancelar"
  btnCancelar.addEventListener('click', () => {
    modal.close();
  });

  // Fechar clicando fora da caixa
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.close();
    }
  });