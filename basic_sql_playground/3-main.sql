/*Upade age of some person*/
update Person set age = '27' where first_name = 'Jon' and last_name = 'Snow';
update Person set age = '18' where first_name = 'Walter Junior' and last_name = 'White';
/*Delete 'Walter White' from both tables*/
/*First delete the foreign key in EyesColor table and then delete the record from Person table*/
delete from EyesColor where person_id = (select id from Person where first_name = 'Walter' and last_name = 'White');
delete from Person where first_name = 'Walter' and last_name = 'White';
select * from Person order by first_name;
