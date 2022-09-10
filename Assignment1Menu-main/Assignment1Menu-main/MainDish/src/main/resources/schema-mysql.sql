USE `maindishlister-db`;

create table if not exists maindish(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    mainDishId INTEGER NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    price DOUBLE NOT NULL,
    description VARCHAR(255) NOT NULL
) engine=InnoDB;