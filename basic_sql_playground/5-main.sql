/*all distinct last_name of the TVShow = Game of Thrones ordered by last_name ascending*/
select last_name from Person where id = (select person_id from TVShowPerson where tvshow_id = (select id from TVShow where name = 'Game of Thrones'));
/*the number of Person where the age is greater than 30*/
select count(*) from Person where age > 30;
/*all Person records with all information from all tables*/
select Person.id, first_name, last_name, age, color, name
from Person LEFT JOIN EyesColor on Person.id = EyesColor.person_id
LEFT JOIN TVShowPerson on Person.id = TVShowPerson.person_id
LEFT JOIN TVShow on TVShowPerson.tvshow_id = TVShow.id;
/*the sum of age of all Person*/
select sum(age) from Person;
