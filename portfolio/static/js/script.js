document.addEventListener(
    'DOMContentLoaded', function () {
        const navOpen = document.getElementById('nav-open');
        const navClose = document.getElementById('nav-close');
        const navLinks = document.getElementById('nav-links');

        navOpen.addEventListener('click', function () {
            navLinks.classList.add('active');
            navClose.classList.add('display');
            navOpen.classList.add('hide');
        });

        navClose.addEventListener('click', function () {
            navLinks.classList.remove('active');
            navClose.classList.remove('display');
            navOpen.classList.remove('hide');
        });
    }
)