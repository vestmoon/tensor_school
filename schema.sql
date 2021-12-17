DROP SCHEMA public CASCADE;
CREATE SCHEMA public;



insert into Course (id, name, endpoint, button_img, description, img_src) values ('1', 'Проектирование', 'design', 'icons/Design.png', 'Этот курс посвящен тому, чтобы ты научился планировать '
                                                             'и оценивать свои задумки, составлять требования к '
                                                             'будующим проектам, научился строить макеты и прототипы, '
                                                             'а также их тестировать!', '../static/computer.png');
insert into Course (id, name, endpoint, button_img, description, img_src) values ('2', 'Frontend', 'frontend', 'icons/CodeFile.png', 'Этот курс посвящен тому, чтобы ты научился делать фронтенд!', '../static/computer.png');
insert into Course (id, name, endpoint, button_img, description, img_src) values ('3', 'Backend', 'backend', 'icons/back.png', 'Этот курс посвящен тому, чтобы ты научился делать бэкэнд!!', '../static/computer.png');
insert into Course (id, name, endpoint, button_img, description, img_src) values ('4', 'Тестирование', 'testing', 'icons/Ok.png', 'Этот курс посвящен тому, чтобы ты научился делать тестирование!', '../static/computer.png');
insert into Course (id, name, endpoint, button_img, description, img_src) values ('5', 'Базы данных', 'databases', 'icons/Database.png', 'Этот курс посвящен тому, чтобы ты научился делать базы данных!!', '../static/computer.png');
insert into Course (id, name, endpoint, button_img, description, img_src) values ('6', 'CI/CD', 'CICD', 'icons/Synchronize.png', 'Этот курс посвящен тому, чтобы ты научился CI/CD!', '../static/computer.png');




insert into bonus (id, description, img_src) values('1', '10 подробных лекций с материалами', 'icons/Circled 10.png');
insert into bonus (id, description, img_src) values('2', 'Сертификат о прохождении курса', 'icons/Diploma.png');
insert into bonus (id, description, img_src) values('3', 'Коллекцию новых работ в свое портфолио', 'icons/Resume.png');

insert into association (course_id, bonus_id) values (1, 1);
insert into association (course_id, bonus_id) values (1, 2);
insert into association (course_id, bonus_id) values (1, 3);
insert into association (course_id, bonus_id) values (2, 1);
insert into association (course_id, bonus_id) values (2, 2);
insert into association (course_id, bonus_id) values (2, 3);
insert into association (course_id, bonus_id) values (3, 1);
insert into association (course_id, bonus_id) values (3, 2);
insert into association (course_id, bonus_id) values (3, 3);
insert into association (course_id, bonus_id) values (4, 1);
insert into association (course_id, bonus_id) values (4, 2);
insert into association (course_id, bonus_id) values (4, 3);
insert into association (course_id, bonus_id) values (5, 1);
insert into association (course_id, bonus_id) values (5, 2);
insert into association (course_id, bonus_id) values (5, 3);
insert into association (course_id, bonus_id) values (6, 1);
insert into association (course_id, bonus_id) values (6, 2);
insert into association (course_id, bonus_id) values (6, 3);