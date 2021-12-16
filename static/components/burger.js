const main = document.querySelector('.main');
const burger = document.querySelector('.header__burger');
const nav = document.querySelector('.navigation');
const links = document.querySelectorAll('.navigation__element');
function slider() {
   burger.addEventListener('click', () => {
       nav.classList.toggle('nav-active');
       burger.classList.toggle('burger-open');    
   })
   main.addEventListener('click', () => {
    nav.classList.remove('nav-active');
    burger.classList.remove('burger-open');    
})
}

slider();