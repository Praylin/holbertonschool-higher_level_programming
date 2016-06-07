/*Add EyesColor */
insert into EyesColor (person_id, color) values ((select id from Person where first_name = 'Jon' and last_name = 'Snow'), ('Brown'));
insert into EyesColor (person_id, color) values ((select id from Person where first_name = 'Arya' and last_name = 'Stark'), ('Green'));
/*Create table TVShow*/
create table TVShow
(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name char(128) NOT NULL
);
/*Create table TVShowPerson*/
create table TVShowPerson
(
  tvshow_id INTEGER NOT NULL,
  person_id INTEGER NOT NULL,
  FOREIGN KEY(tvshow_id) REFERENCES TVShow(id),
  FOREIGN KEY(person_id) REFERENCES Person(id)
);
/*Insert values in TVShow*/
insert into TVShow (name) values ('Homeland');
insert into TVShow (name) values ('The big bang theory');
insert into TVShow (name) values ('Game of Thrones');
insert into TVShow (name) values ('Breaking bad');
/*Insert values in TVShowPerson*/
insert into TVShowPerson (person_id, tvshow_id) values ((select id from Person where first_name = 'Walter Junior' and last_name = 'White'), (select id from TVShow where name = 'Breaking bad'));
insert into TVShowPerson (person_id, tvshow_id) values ((select id from Person where first_name = 'Jaime' and last_name = 'Lannister'), (select id from TVShow where name = 'Game of Thrones'));
insert into TVShowPerson (person_id, tvshow_id) values ((select id from Person where first_name = 'Sheldon' and last_name = 'Cooper'), (select id from TVShow where name = 'The big bang theory'));
insert into TVShowPerson (person_id, tvshow_id) values ((select id from Person where first_name = 'Tyrion' and last_name = 'Lannister'), (select id from TVShow where name = 'Game of Thrones'));
insert into TVShowPerson (person_id, tvshow_id) values ((select id from Person where first_name = 'Jon' and last_name = 'Snow'), (select id from TVShow where name = 'Game of Thrones'));
insert into TVShowPerson (person_id, tvshow_id) values ((select id from Person where first_name = 'Arya' and last_name = 'Stark'), (select id from TVShow where name = 'Game of Thrones'));
/*Display all tables*/
select * from Person;
select * from EyesColor;
select * from TVShow;
select * from TVShowPerson;
