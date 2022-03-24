create database SQL_Bootcamp;
use SQL_Bootcamp;

/*1. Write an SQL query to report the managers with at least five direct reports*/
CREATE TABLE managers (
	    id int,
            name varchar(255),
            department varchar(255),
            managerid varchar(255) );            
INSERT INTO managers (id, name, department, managerid) 
		VALUES ('101', 'John', 'A', ' '),
			('102', 'Dan','A', '101'),
               		('103', 'James', 'A', '101'),
               		('104', 'Amy' ,'A', '101'),
               		('105', 'Anne', 'A', '101'),
               		('106', 'Ron', 'A', '101');			
SELECT name FROM managers WHERE id IN (SELECT managerid FROM managers GROUP BY managerid HAVING COUNT(*) >= 5);

/*2. Write an SQL query to report the nth highest salary from the Employee table.
If there is no nth highest salary, the query should report null*/
CREATE TABLE employee (
			id int,
            		salary int);
INSERT INTO employee (id, salary)
		VALUES ('1', '100'),
			('2', '200'),
                	('3', '300');                
SELECT DISTINCT(salary) as "getNthHighestSalary(2)" FROM employee ORDER BY salary DESC LIMIT 1 OFFSET 1;
DELETE FROM employee WHERE salary > 100;
SELECT DISTINCT(salary) as "getNthHighestSalary(2)" FROM employee ORDER BY salary DESC LIMIT 1 OFFSET 1;

/*3. Write an SQL query to find the people who have the most friends and the most friends number*/
CREATE TABLE friends (
		    requested_id int NOT NULL,
                    accepter_id int NOT NULL,
                    accept_date date,
                    PRIMARY KEY (requested_id, accepter_id));                    
INSERT INTO friends (requested_id, accepter_id, accept_date)
	VALUES ('1','2','2016/06/03'),
			('1','3','2016/06/08'),
            ('2','3','2016/06/08'),
            ('3','4','2016/06/09');
SELECT id, COUNT(id) AS num FROM (
			SELECT requested_id AS id 
                        FROM friends
                        UNION ALL
                        SELECT accepter_id AS id
                        FROM friends
                        ) AS total_table GROUP BY id ORDER BY COUNT(id) DESC LIMIT 1;
                        
/*4. Write an SQL query to swap the seat id of every two consecutive students.
If the number of students is odd, the id of the last student is not swapped*/
CREATE TABLE students (
			id int NOT NULL,
                       name varchar(255),
                       PRIMARY KEY (id));
INSERT INTO students (id, name)
	   VALUES ('1', 'Abbie'),
		('2','Doris'),
               ('3','Emerson'),
               ('4','Green'),
               ('5','Jeames');
SELECT IF(id<(SELECT MAX(id) FROM students),IF(id%2=0,id-1, id+1),IF(id%2=0, id-1, id)) 
			AS id, name FROM students ORDER BY id;
            
/*5. Write an SQL query to report the customer ids from the Customer table that bought all the products in the Product table*/
CREATE TABLE customer (
			customer_id int,
                        product_key int) ;
CREATE TABLE product (
		     product_key int NOT NULL,
                      PRIMARY KEY (product_key)) ;
INSERT INTO customer (customer_id, product_key)
		VALUES ('1','5'),
		('2','6'),
                ('3','5'),
                ('3','6'),
                ('1','6');
INSERT INTO product (product_key)
		VALUES ('5'),
			('6');
SELECT a.customer_id FROM (SELECT customer_id, COUNT(DISTINCT product_key) 
AS num FROM customer GROUP BY customer_id) a WHERE a.num = (SELECT COUNT(DISTINCT product_key) FROM product);

/*6. Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019*/
CREATE TABLE users (
		    user_id int NOT NULL,
                    join_date date,
                    favorite_brand varchar(255),
                    PRIMARY KEY(user_id));
CREATE TABLE orders (
		    order_id int NOT NULL,
                    order_date date,
                    item_id int NOT NULL,
                    buyer_id int,
                    seller_id int,
                    PRIMARY KEY (order_id),
                    FOREIGN KEY (item_id) REFERENCES items(item_id),
                    FOREIGN KEY (buyer_id) REFERENCES users(user_id),
                    FOREIGN KEY (seller_id) REFERENCES users(user_id));
CREATE TABLE items (
		    item_id int NOT NULL,
                    item_brand varchar(255),
                    PRIMARY KEY (item_id));
INSERT INTO users (user_id, join_date, favorite_brand)
		VALUES ('1','2018-01-01','Lenovo'),
		       ('2','2018-02-09','Samsung'),
                       ('3','2018-01-19','LG'),
                       ('4','2018-05-21','HP');
INSERT INTO orders (order_id, order_date, item_id, buyer_id, seller_id)
		VALUES ('1','2019-08-01','4','1','2'),
		       ('2','2018-08-02','2','1','3'),
               		('3','2019-08-03','3','2','3'),
               		('4','2018-08-04','1','4','2'),
               		('5','2018-08-04','1','3','4'),
               		('6','2019-08-05','2','2','4');
INSERT INTO items (item_id, item_brand)
		VALUES ('1','Samsung'),
		('2','Lenovo'),
                ('3','LG'),
                ('4','HP');
SELECT user_id buyer_id, join_date, IFNULL(num,0) AS orders_in_2019 FROM users
			LEFT JOIN (SELECT buyer_id, COUNT(*) AS num FROM orders 
            WHERE order_date BETWEEN DATE('2019-01-01') AND DATE('2019-12-31')
            GROUP BY buyer_id) 
            AS t ON users.user_id=t.buyer_id;
            
/*7. Write an SQL query to reports for every date within at most 90 days from today, 
the number of users that logged in for the first time on that date. Assume today is 2019-06-30*/
CREATE TABLE traffic (
			user_id int,
                      activity enum ('login', 'logout', 'jobs', 'groups', 'homepage'),
                      activity_date date);
INSERT INTO traffic (user_id, activity, activity_date)
		VALUES ('1','login','2019-05-01'),
		('1', 'homepage','2019-05-01'),
                ('1','logout','2019-05-01'),
                ('2','login','2019-06-21'),
                ('2','logout','2019-06-21'),
                ('3','login','2019-01-01'),
                ('3','jobs','2019-01-01'),
                ('3','logout','2019-01-01'),
                ('4','login','2019-06-21'),
                ('4','groups','2019-06-21'),
                ('4','logout','2019-06-21'),
                ('5','login','2019-03-01'),
                ('5','logout','2019-03-01'),
                ('5','login','2019-06-21'),
                ('5','logout','2019-06-21');
SELECT login_date, COUNT(user_id) AS user_count
FROM (SELECT user_id, MIN(activity_date) AS login_date
    FROM traffic
    WHERE activity = 'login'
    GROUP BY user_id) AS t
WHERE login_date >= DATE_ADD('2019-06-30', INTERVAL -90 DAY) AND login_date <= '2019-06-30'
GROUP BY login_date;
                
/*8. Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10*/
CREATE TABLE Products (
			product_id int NOT NULL,
                        new_price int,
                        change_date date NOT NULL,
                        PRIMARY KEY (product_id, change_date));
INSERT INTO Products (product_id, new_price, change_date)
		VALUES ('1','20','2019-08-14'),
		('2','50','2019-08-14'),
                ('1','30','2019-08-15'),
                ('1','35','2019-08-16'),
                ('2','65','2019-08-17'),
                ('3','20','2019-08-18');
SELECT * FROM 
(SELECT product_id, new_price AS price FROM Products
 WHERE (product_id, change_date) IN (
                                     SELECT product_id, MAX(change_date)
                                     FROM Products
                                     WHERE change_date <= '2019-08-16'
                                     GROUP BY product_id)

 UNION

 SELECT DISTINCT product_id, 10 AS price
 FROM Products
 WHERE product_id NOT IN (SELECT product_id FROM Products WHERE change_date <= '2019-08-16')
) tmp
ORDER BY price DESC;

/*9. Write an SQL query to find for each month and country: the number of approved 
transactions and their total amount, the number of chargebacks, and their total amount*/
CREATE TABLE transactions (
			    id int NOT NULL,
                            country varchar(255),
                            state enum ('approved','declined'),
                            amount int,
                            trans_date date,
                            PRIMARY KEY (id));
CREATE TABLE chargebacks (
			    trans_id int NOT NULL,
                            trans_date date,
                            FOREIGN KEY (trans_id) REFERENCES transactions(id));
INSERT INTO transactions (id, country, state, amount, trans_date)
		VALUES  ('101','US','approved','1000','2019-05-18'),
		('102','US','declined','2000','2019-05-19'),
                ('103','US','approved','3000','2019-06-10'),
                ('104','US','declined','4000','2019-06-13'),
                ('105','US','approved','5000','2019-06-15');
INSERT INTO chargebacks (trans_id, trans_date)
		VALUES ('102','2019-05-29'),
		('101','2019-06-30'),
                ('105','2019-09-18');
SELECT month, country,
    SUM(CASE WHEN type='approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(CASE WHEN type='approved' THEN amount ELSE 0 END) AS approved_amount,
    SUM(CASE WHEN type='chargeback' THEN 1 ELSE 0 END) AS chargeback_count,
    SUM(CASE WHEN type='chargeback' THEN amount ELSE 0 END) AS chargeback_amount
FROM (
    (
    SELECT left(t.trans_date, 7) AS month, t.country, amount,'approved' AS type
    FROM transactions AS t
    WHERE state='approved'
    )
    UNION ALL (
    SELECT left(c.trans_date, 7) AS month, t.country, amount,'chargeback' AS type
    FROM transactions AS t JOIN chargebacks AS c
    ON t.id = c.trans_id
    )
) AS tt
GROUP BY tt.month, tt.country;

/*10. Write an SQL query that selects the team_id, team_name and num_points 
of each team in the tournament after all described matches*/
CREATE TABLE teams (
		    team_id int NOT NULL,
                    team_name varchar(255),
                    PRIMARY KEY (team_id));
CREATE TABLE matches (
		      match_id int NOT NULL,
                      host_team int,
                      guest_team int,
                      host_goals int,
                      guest_goals int,
                      PRIMARY KEY (match_id));
INSERT INTO teams (team_id, team_name)
		VALUES ('10','Leetcode FC'),
		('20','NewYork FC'),
                ('30','Atlanta FC'),
                ('40','Chicago FC'),
                ('50','Toronto FC');
INSERT INTO matches (match_id, host_team, guest_team, host_goals, guest_goals)
		VALUES ('1','10','20','3','0'),
		('2','30','10','2','2'),
                ('3','10','50','5','1'),
                ('4','20','30','1','0'),
                ('5','50','30','1','0');
SELECT teams.team_id, teams.team_name,
    SUM(CASE WHEN team_id=host_team AND host_goals>guest_goals THEN 3 ELSE 0 END) +
    SUM(CASE WHEN team_id=host_team AND host_goals=guest_goals THEN 1 ELSE 0 END) +
    SUM(CASE WHEN team_id=guest_team AND host_goals<guest_goals THEN 3 ELSE 0 END) +
    SUM(CASE WHEN team_id=guest_team AND host_goals=guest_goals THEN 1 ELSE 0 END) AS num_points
FROM teams LEFT JOIN matches
ON teams.team_id = matches.host_team OR teams.team_id = matches.guest_team
GROUP BY teams.team_id
ORDER BY num_points DESC, teams.team_id ASC ;
