CREATE DATABASE expense_monitoring;
USE expense_monitoring;
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50)
);

CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2),
    expense_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
INSERT INTO users(name,email)
VALUES
('Reshmi','reshmi@gmail.com'),
('Aarav','aarav@gmail.com');

INSERT INTO categories(category_name)
VALUES
('Food'),
('Travel'),
('Shopping'),
('Bills');

INSERT INTO expenses(user_id,category_id,amount,expense_date)
VALUES
(1,1,250,'2026-01-10'),
(1,2,500,'2026-01-12'),
(2,3,1200,'2026-01-13'),
(1,4,800,'2026-01-15');
SELECT * FROM users;
SELECT * FROM categories;
SELECT * FROM expenses;
UPDATE expenses
SET amount = 900
WHERE expense_id = 4;
SELECT * FROM expenses;
DELETE FROM expenses
WHERE expense_id = 2;
SELECT * FROM expenses;
DELIMITER //

CREATE PROCEDURE MonthlyExpenseSummary()
BEGIN
    SELECT 
        c.category_name,
        SUM(e.amount) AS total_expense
    FROM expenses e
    JOIN categories c
    ON e.category_id = c.category_id
    GROUP BY c.category_name;
END //

DELIMITER ;
CALL MonthlyExpenseSummary();










