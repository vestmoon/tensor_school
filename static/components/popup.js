class Popup {
    constructor() {
        this.container = document.createElement('div');
        this.container.className = 'popup';
        this.container.innerHTML = this.render();
        this.insert();
        button.addEventListener(
            'click', function () {popup.open()}
        );
    }

    render() {  return `
        <div class="popup__body">
            <div class="popup__content">
                <div class="popup__title">Заполни анкету, чтобы<br>записаться на курс</div>
                <a href="#header" class="popup__close close-popup">X</a>
                <form class="form" method="post" enctype="multipart/form-data">
                    <div class="form__item">
                        <div class="form__label">ФИО</div>
                        <input class="form__input" name="user_fio" type="text" placeholder="Петров Василий Иванович">
                    </div>
                    <div class="form__item">
                        <div class="form__label">Город</div>
                        <input class="form__input" name="user_city" type="text" placeholder="г.Уфа">
                    </div>
                    <div class="form__item">
                        <div class="form__label">Номер телефона для связи</div>
                        <input class="form__input" name="user_number" type="text" placeholder="+7-(...)-...-..-..">
                    </div>
                    <div class="form__item">
                        <div class="form__label">Электронная почта</div>
                        <input class="form__input" name="user_mail" type="text" placeholder="tensor@mail.com"">
                    </div>
                    <input class="popup__button button" type="submit" value="Отправить">
                </form>
            </div>
        </div>
        `
    }
    hide() {
        this.container.classList.remove('open');
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
        this.container.classList.add('open');
    }
    destroy() {
        this.container.remove();
    }

}

const wrapper = document.querySelector('.wrapper');
const button = document.querySelector('.popup-link');

const popup = new Popup();


