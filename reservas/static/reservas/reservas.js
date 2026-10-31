const modal = document.getElementById('modalReserva');
const btnAbrir = document.getElementById('btnNovaReserva');
const btnFechar = document.getElementById('btnFecharModal');
const btnCancelar = document.getElementById('btnCancelar');

if (modal) {
  if (btnAbrir) btnAbrir.addEventListener('click', () => modal.showModal());
  if (btnFechar) btnFechar.addEventListener('click', () => modal.close());
  if (btnCancelar) btnCancelar.addEventListener('click', () => modal.close());

  modal.addEventListener('click', (e) => {
    if (e.target !== modal) return;
    const r = modal.getBoundingClientRect();
    const fora = e.clientX < r.left || e.clientX > r.right ||
                 e.clientY < r.top || e.clientY > r.bottom;
    if (fora) modal.close();
  });

  if (modal.dataset.abrir === '1') modal.showModal();
}