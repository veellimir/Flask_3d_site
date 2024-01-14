const success = document.querySelector('.success');

function closeSuccess() {
    if (success) {
        success.style.opacity = 0;
    }
};

setTimeout( () => {closeSuccess();}, 2000);
