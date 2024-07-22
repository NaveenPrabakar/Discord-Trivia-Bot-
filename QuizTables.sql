use discordbot;

-- Creating the tables for the question bank
Create Table cote(
question varchar(200),
answer1 varchar(200),
answer2 varchar(200),
answer3 varchar(200),
correct varchar(200),
primary key(question)
);

-- Stores picture locations of the anime
Create Table pictures(
anime varchar(200),
picture varchar(200),

primary key(picture)
);

-- Stores userData
Create Table userData(
UserID varchar(100),
correct Integer,
total Integer,
anime varchar(200),

primary key(UserID, anime)
);
