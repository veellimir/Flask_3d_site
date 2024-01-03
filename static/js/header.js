const icBasket = document.querySelector('.basket'),
      modalBasket = document.querySelector('.wrapper_basket'),
      itemBasket = document.querySelector('.modal_basket');

icBasket.addEventListener('click', () => {
    modalBasket.classList.add('wrapper_basket_active');
    itemBasket.classList.add('modal_basket_active');
})

modalBasket.addEventListener('click', () => {
    modalBasket.classList.remove('wrapper_basket_active');
    itemBasket.classList.remove('modal_basket_active');
})


let header = document.querySelector('header'),
    headerH = document.querySelector('header').clientHeight,
    social = document.querySelector('.social');

    document.onscroll = function () {
        let scroll = window.scrollY
        
        if (scroll > headerH) {
            header.classList.add('active_header')
            social.style.display = 'none'
        }
        else {
            header.classList.remove('active_header')
            social.style.display = 'block'
        }
    }
    