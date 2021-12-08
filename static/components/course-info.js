class CourseInfo {
    constructor(title, description, courseAdvantageArray){
        this.container = document.createElement('div');
        this.container.className = 'designing';
        this.container.innerHTML = this.render(title, description, courseAdvantageArray); 
    }
    
    render(title, description, courseAdvantageArray) { return `        
            <h2 class="header">${title,title}</h2>	
            <p class="description">${description}</p>				
    
            <div class="bonuses">
                <a class="header">А также, ты получишь:</a>        
                <div class="list">${courseAdvantageArray.place()}</div>
            </div>  

            <div class="signUp">
                <a class="signUp__button" href="tensor.html">Записаться</a>
            </div>
		`
    }

    show(container) {        
        container.insertAdjacentElement('beforeend', this.container);
    }
}
class CourseAdvantage {
    constructor(icon,text){
        this.container = document.createElement('div');
        this.container.className = 'list__element';          
        this.container.innerHTML = this.render(icon,text); 
    }

    render(icon,text) { return `
            <img class="courseimg" src="${icon}"/>
            <div class="text">${text}</div>
        `
    }

    place() {
        return this.container.outerHTML;
    }
}

class CourseAdvantageArray {
    array;
    constructor(){
        this.array= new Array();
    }
    add(courseAdvantage) {
        this.array.push(courseAdvantage);
    }
    place() {
        for(let i in this.array)
        {
            console.log(this.array[i].place());
            return  this.array[i].place();

        }
       
    }
}
const container = document.querySelector('.courseCard');
const courseAdvantageArray = new CourseAdvantageArray()
courseAdvantageArray.add(new CourseAdvantage('../static/icons/Circled 10.png', '10 подробных лекций  с материалами'));
courseAdvantageArray.add(new CourseAdvantage('../static/icons/Circled 10.png', '10 подробных лекций  с материалами'));
// const courseAdvantage = new CourseAdvantage('icons/Circled 10.png', '10 подробных лекций  с материалами');
const courseInfo = new CourseInfo('Проектирование', 'Этот курс посвящен тому, чтобы ты научился планировать и оценивать свои задумки, составлять требования к будующим проектам, научился строить макеты и прототипы, а также их тестировать!', courseAdvantageArray);


courseInfo.show(container);

