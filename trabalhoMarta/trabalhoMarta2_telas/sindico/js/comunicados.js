const modal = document.getElementById('modalComunicado');
const btnAbrir = document.getElementById('btnNovoComunicado');
const btnFechar = document.getElementById('btnFecharModal');
const btnCancelar = document.getElementById('btnCancelar');

// Abrir o modal
btnAbrir.addEventListener('click', () => {
    modal.showModal();
});

// Fechar no botão X
btnFechar.addEventListener('click', () => {
    modal.close();
});

// Fechar no botão Cancelar
btnCancelar.addEventListener('click', () => {
    modal.close();
});

// Fechar ao clicar fora (no backdrop)
modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.close();
    }
});
