class CourseCard {
    constructor(icon, title, href){
        this.container = document.createElement('a');
        this.container.href = href;
        this.container.className = 'course';          
        this.container.innerHTML = this.render(icon, title); 
    }
    
    render(icon, title) { return `        
			<img class="course__img" src="${icon}"/>
			<a class="course__name">${title}</a>
		`
    }

    show(container) {       
        container.insertAdjacentElement('beforeend', this.container);
    }
}

//const container = document.querySelector('.courses-block');
//const options= [
//    {icon: "../static/icons/CodeFile.png",    title: 'Frontend',          href: '/frontend'},
//    {icon: '../static/icons/Design.png',      title: 'Проектирование',    href: '/design'},
//    {icon: '../static/icons/back.png',        title: 'Backend',           href: '/backend'},
//    {icon: '../static/icons/Ok.png',          title: 'Тестирование',      href: 'tensor.html'},
//    {icon: '../static/icons/Database.png',    title: 'Базы данных',       href: 'tensor.html'},
//    {icon: '../static/icons/Synchronize.png', title: 'CI/CD',             href: 'tensor.html'}
//];
//const courseCardArray = Array();
//
//// let key;
//for(key in options) {
//    courseCardArray[key] = new CourseCard(options[key].icon, options[key].title, options[key].href);
//    courseCardArray[key].show(container);
//}
