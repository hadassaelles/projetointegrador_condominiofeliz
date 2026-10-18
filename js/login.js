const form = document.getElementById("formLogin");
const mensagem = document.getElementById("mensagem");

const usuarios = [
    {
        nome: "morador",
        senha: "condominio123",
        pagina: "/morador/home.html"
    },
    {
        nome: "sindico",
        senha: "condominio123",
        pagina: "/sindico/home.html"
    },
    {
        nome: "funcionario",
        senha: "condominio123",
        pagina: "/funcionario/home.html"
    }
];

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value;
    const senha = document.getElementById("senha").value;

    const usuarioEncontrado = usuarios.find(function(usuario) {
        return usuario.nome === nome &&
               usuario.senha === senha;
    });

    if (usuarioEncontrado) {
        window.location.href = usuarioEncontrado.pagina;
    } else {
        mensagem.textContent = "Usuário ou senha incorretos!";
    }
});
