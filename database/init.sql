CREATE TABLE IF NOT EXISTS song (
    title varchar(30) not null,
    artist varchar(30) not null,
    price int not null,
    album varchar(30),
    song_id varchar(30) not null,
    release_year int not null,
    primary key(song_id)
);

CREATE TABLE IF NOT EXISTS album (
    title varchar(30) not null,
    artist varchar(30) not null,
    price int not null,
    album_id varchar(30) not null,
    release_year int not null,
    primary key(album_id)
);

CREATE TABLE IF NOT EXISTS users (
    username varchar(30) not null,
    password varchar(30) not null,
    PRIMARY KEY(username)
);

CREATE TABLE IF NOT EXISTS admins (
    username varchar(30) not null,
    password varchar(30) not null,
    PRIMARY KEY(username)
);

INSERT INTO song(title, artist, price, album, song_id, release_year) VALUES
    ('After Hours', 'The Weeknd', 1, 'After Hours', 1000, 2020),
    ('Heartless', 'The Weeknd', 1, 'After Hours', 1001, 2020),
    ('In Your Eyes', 'The Weeknd', 1, 'After Hours', 1002, 2020),
    ('Blinding Lights', 'The Weeknd', 1, 'After Hours', 1003, 2020),
    ('Faith', 'The Weeknd', 1, 'After Hours', 1004, 2020),
    ('Too Late', 'The Weeknd', 1, 'After Hours', 1005, 2020),
    ('A Place Without Name', 'Michael Jackson', 1, 'Xscape', 1100, 2014),
    ('This Is America', 'Childish Gambino', 1, null, 1200, 2018);

INSERT INTO album(title, artist, price, album_id, release_year) VALUES
    ('After Hours', 'The Weeknd', 30, 10000, 2020),
    ('Starboy', 'The Weeknd', 30, 10001, 2016),
    ('My Dear Melancholy,', 'The Weeknd', 30, 10002, 2018),
    ('Invincible', 'Michael Jackson', 30, 10003, 2001),
    ('Dangerous', 'Michael Jackson', 30, 10004, 1991),
    ('Bad', 'Michael Jackson', 30, 10005, 1987),
    ('HIStory', 'Michael Jackson', 30, 10006, 1995),
    ('Thriller', 'Michael Jackson', 30, 10007, 1982),
    ('Music To Be Murdered By', 'Eminem', 30, 10008, 2020);

INSERT INTO users(username, password) VALUES
    ('florin', 'muenan'),
    ('deea', 'chica'),
    ('andreea', 'pika_pika');