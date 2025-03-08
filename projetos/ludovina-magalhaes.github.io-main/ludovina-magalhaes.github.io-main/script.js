
document.addEventListener('DOMContentLoaded', () => 
{
    const menuMobile = document.querySelector('.menu-mobile');
    const btnFechar = document.querySelector('.btn-fechar');
    const menuIcon = document.querySelector('#menu-icon');

    // Função para abrir o menu
    function abrirMenu() {
        menuMobile.classList.add('active'); // Adiciona a classe 'active'
    }

    // Função para fechar o menu
    function fecharMenu() {
        menuMobile.classList.remove('active'); // Remove a classe 'active'
    }

    // Adiciona o evento de abrir o menu ao ícone do menu
    if (menuIcon) {
        menuIcon.addEventListener('click', abrirMenu);
    }

    // Adiciona o evento de fechar o menu ao botão de fechar
    if (btnFechar) {
        btnFechar.addEventListener('click', fecharMenu);
    }

    // Fecha o menu ao clicar em um link do menu
    const menuLinks = document.querySelectorAll('.menu-mobile nav a');
    menuLinks.forEach(link => {
        link.addEventListener('click', fecharMenu); // Fecha o menu ao clicar em qualquer link
    });
});

document.querySelectorAll('.mobile-title a').forEach(function(link) 
{
    link.addEventListener('click', function(event) 
    {
        window.open(link.href, '_blank');
    });
});