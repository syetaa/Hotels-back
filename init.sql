CREATE TABLE IF NOT EXISTS room
(
    id SERIAL PRIMARY KEY,
    city VARCHAR,
    hotel VARCHAR,
    price INT,
    capacity INT
);

CREATE TABLE IF NOT EXISTS "user"
(
    id SERIAL PRIMARY KEY,
    username VARCHAR, 
    name VARCHAR,
    surname VARCHAR,
    email VARCHAR,
    password VARCHAR
);

CREATE TABLE IF NOT EXISTS "order"
(
    id SERIAL PRIMARY KEY,
    user_id INT references "user"(id),
    room_id INT references room(id)
);

CREATE TABLE IF NOT EXISTS bookmark
(
    id SERIAL PRIMARY KEY,
    user_id INT references "user"(id),
    room_id INT references room(id)
);

