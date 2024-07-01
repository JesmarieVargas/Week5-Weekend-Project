
CREATE DATABASE LibraryManagementSystem;

SELECT * FROM books;
SELECT * From users;

CREATE TABLE books(
id INT AUTO_INCREMENT PRIMARY KEY,
book_title VARCHAR(100) NOT NULL,
book_author VARCHAR(50) NOT NULL,
availability VARCHAR(25) DEFAULT "available for rent"
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(16) NOT NULL
);

CREATE TABLE borrowed_books(
	id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT NOT NULL,
    book_id INT NOT NULL,
    title VARCHAR(100),
    borrow_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO users (user_name, email, phone)
VALUES ('Trey Quinn', 'TQuinn@gmail.com', '977-165-2165'),
('Valerie Mclean', 'Val5674@gmail.com', '828-458-9652'),
('Reid Holman', 'HolmanR78@gmail.com', '854-215-1811');

INSERT INTO books (book_title, book_author)
VALUES ('Harry Potter', 'J.K. Rowlings'),
('101 Dalmations', 'Dodie Smith');

DROP TABLE books;
DROP TABLE borrowed_books;
