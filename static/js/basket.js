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
