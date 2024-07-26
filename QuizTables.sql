use discordbot;

-- Creating the tables for the question bank

-- Table for the anime (Cote)
Create Table cote(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

-- Table for the anime black clover
Create Table blackclover(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

-- Table for the anime naruto
Create Table naruto(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

-- Table for the game genshin
Create Table genshin(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

-- table for the anime bleach
Create Table bleach(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table onepiece(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table roshidere(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table toradora(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table toradora(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table intiald(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table eminanceinshadow(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table attackontitan(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table hunterxhunter(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table jjk(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table deathnote(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table demonslayer(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table drstone(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table fate(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table aoaishi(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table bluelock(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
primary key(question)
);

Create Table haikyuu(
question varchar(500),
answer1 varchar(500),
answer2 varchar(500),
answer3 varchar(500),
correct varchar(500),
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

