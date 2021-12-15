const burger = document.querySelector('.burger');
const nav = document.querySelector('.navigation');
const links = document.querySelectorAll('.navigation__element');
function slider() {
   burger.addEventListener('click', () => {
       nav.classList.toggle('nav-active');
       burger.classList.toggle('toggle');    
   })
}

slider();