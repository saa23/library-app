-- user database
CREATE TABLE perpustakaan_project.customers (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    UNIQUE (username,email)
);

-- inserting the user data
INSERT INTO perpustakaan_project.customers(username,firstname,lastname,email) 
VALUES  ("userpertama","rudi","roundhouse","rudi.roundhouse@gmail.com"),
        ("userkedua","shiroe","ishigami","shiroe.ishigami@gmail.com"),
        ("userketiga","akatsuki","horizon","akatsuki.horizon@gmail.com");


-- transaction (borrow) database
CREATE TABLE perpustakaan_project.borrows (
    borrowid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    borrowdate DATETIME NOT NULL,
    userid INT NOT NULL,
    bookid VARCHAR(45) NOT NULL,
    bookname VARCHAR(255) NULL,
    isactive TINYINT NULL,
    INDEX userid_idx (userid ASC) VISIBLE,
    CONSTRAINT userid
    FOREIGN KEY (userid)
    REFERENCES perpustakaan_project.customers(userid)
    );