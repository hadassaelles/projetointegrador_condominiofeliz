const modal = document.getElementById('modalReserva');
const btnAbrir = document.getElementById('btnNovaReserva'); // ID do botão que abre o pop-up
const btnFechar = document.getElementById('btnFecharModal');
const btnCancelar = document.getElementById('btnCancelar');

// Abrir o modal
btnAbrir.addEventListener('click', () => {
  modal.showModal();
});

// Fechar o modal no botão "X"
btnFechar.addEventListener('click', () => {
  modal.close();
});

// Fechar o modal no botão "Cancelar"
btnCancelar.addEventListener('click', () => {
  modal.close();
});

// Fechar ao clicar na área externa (backdrop)
modal.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.close();
  }
});