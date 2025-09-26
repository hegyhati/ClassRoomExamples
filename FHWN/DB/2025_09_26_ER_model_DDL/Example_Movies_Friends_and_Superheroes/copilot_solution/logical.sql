
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    size VARCHAR(10)
);

CREATE TABLE Friendships (
    user_id INT,
    friend_id INT,
    PRIMARY KEY (user_id, friend_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (friend_id) REFERENCES Users(id)
);

CREATE TABLE Pages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(100)
);

CREATE TABLE Follows (
    user_id INT,
    page_id INT,
    PRIMARY KEY (user_id, page_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (page_id) REFERENCES Pages(id)
);

CREATE TABLE Movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_date DATE
);

CREATE TABLE Actors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Roles (
    actor_id INT,
    movie_id INT,
    character_name VARCHAR(255),
    PRIMARY KEY (actor_id, movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actors(id),
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

CREATE TABLE Costumes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    character VARCHAR(255),
    movie_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

CREATE TABLE Purchases (
    id SERIAL PRIMARY KEY,
    user_id INT,
    costume_id INT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (costume_id) REFERENCES Costumes(id)
);

CREATE TABLE Offers (
    id SERIAL PRIMARY KEY,
    user_id INT,
    costume_id INT,
    sent_at TIMESTAMP,
    expires_at TIMESTAMP,
    used BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (costume_id) REFERENCES Costumes(id)
);