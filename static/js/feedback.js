let form = document.querySelector('.form'),
    inputMain = document.querySelectorAll('#inpFeedback');

form.onsubmit = function (event) {
    event.preventDefault();
    let emptyInputs = false;

    inputMain.forEach(function (input) {
        if (input.value.trim() === '') {
            input.classList.add('inputErorr');
            emptyInputs = true; 
        } else {
            input.classList.remove('inputErorr');
        }
    });

    if (emptyInputs) {
        return
    }
    let smsPush = document.querySelector('.sms_push');
    smsPush.classList.add('sms_push_active');
    

    setTimeout(function() {
        form.submit();
    }, 2300);

};