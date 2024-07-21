use discordbot;

Select @@secure_file_priv; -- put all csv files through this directory

-- change directory to whatever you need it to be
Load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\'
into table cote
fields terminated by ','
enclosed by '"'
Lines terminated by '\n'

