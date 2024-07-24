use discordbot;

Select @@secure_file_priv; -- put all csv files through this directory

-- change directory to whatever you need it to be
Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\Book1.csv'
into table cote
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\blackClover.csv'
into table blackclover
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\naruto.csv'
into table naruto
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\genshin.csv'
into table genshin
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\bleach.csv'
into table bleach
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\onepiece.csv'
into table onepiece
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\roshidere.csv'
into table roshidere
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\toradora.csv'
into table toradora
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\intialD.csv'
into table intiald
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';

Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\eminanceInshadow.csv' ignore
into table eminanceinshadow
fields terminated by ','
enclosed by '"'
Lines terminated by '\n';





-- Inserts picture locations to table
Insert into pictures(anime, picture)
Value('cote', 'cote.png');




