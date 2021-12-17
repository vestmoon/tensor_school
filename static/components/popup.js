class Popup {
    constructor() {
        this.container = document.createElement('div');
        this.container.className = 'popup';
        this.container.innerHTML = this.render();
        this.insert();        
    }

    render() {  return `
    <div class="popup__body">
        <div class="popup__content">
            <div class="popup__title">Заполни анкету, чтобы<br>записаться на курс</div>
            <a href="#header" class="popup__close close-popup"><img src="../static/icons/x.png" alt="X"></a>
            <form class="form" method="post" enctype="multipart/form-data" id="form">
                <div class="form__item">
                    <div class="form__label">ФИО</div>
                    <input  id = "name" class="form__input" name="user_fio" type="text" placeholder="Петров Василий Иванович" required>
                </div>
                <div class="form__item">
                    <div class="form__label">Город</div>
                    <input id = "city" class="form__input" name="user_city" type="text" placeholder="г.Уфа" required>
                </div>
                <div class="form__item">
                    <div class="form__label">Номер телефона для связи</div>
                    <label for = "telephone" class = "form__incorrectLabel">Неверный номер телефона</label>
                    <input id = "telephone" class="form__input" name="user_number" type="tel" placeholder="+7-(...)-...-..-.." required>
                </div>
                <div class="form__item">
                    <div class="form__label">Электронная почта</div>
                    <label for = "mail" class = "form__incorrectLabel">Неверная почта</label>
                    <input id = "mail" class="form__input" name="user_mail" type="text" placeholder="tensor@mail.com" required>
                </div>
                <input class="popup__button button" type="submit" value="Отправить">
            </form>
        </div>
    </div>`
    }
    hide() {
        this.container.classList.remove('popup-open');  
    }

    insert() {
        wrapper.insertAdjacentElement('beforeend', this.container);
        const closeLink = document.querySelector('.close-popup');
        closeLink.addEventListener(
            'click',
            (e) => { this.hide(); }
        );
        this.container.addEventListener('click', (e) =>{
            if(!e.target.closest('.popup__content')) {
                this.hide();
            }
        });

    }
    open() {
        this.container.classList.add('popup-open');
    }
    destroy() {
        this.container.remove();
    }

}

const wrapper = document.querySelector('.wrapper');
const button = document.querySelector('.popup-link');
const popup = new Popup();

button.addEventListener(
    'click', function () { popup.open()}
);

const btn = document.querySelector(".popup__button");
btn.addEventListener("click", (e) => {
    let phone_format = /^(\+7|7|8)?\d{10}/;
    let mail_format = /^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$/;
    let checkedPhone = document.getElementById("telephone");
    let checkedMail = document.getElementById("mail");

    if (!phone_format.test(checkedPhone.value)) {
        checkedPhone.previousElementSibling.style.display = "block";
        e.preventDefault();
    } else {
        checkedPhone.previousElementSibling.style.display = "none";
    }
    if (!mail_format.test(checkedMail.value)) {
        checkedMail.previousElementSibling.style.display = "block";
        e.preventDefault();
    } else {
        checkedMail.previousElementSibling.style.display = "none";
    }
});



