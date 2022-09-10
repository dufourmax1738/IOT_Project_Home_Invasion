USE `sidedishlister-db`;

create table if not exists sidedish(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sideDishId INTEGER NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    price DOUBLE NOT NULL,
    description VARCHAR(255) NOT NULL
) engine=InnoDB;