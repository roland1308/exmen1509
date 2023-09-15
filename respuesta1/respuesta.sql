
SELECT count(*) FROM students where age>30;
SELECT * FROM students where color!="amarillo";
SELECT * FROM students where age between 50 and 60;
DROP TABLE students;
SELECT * FROM students WHERE (YEAR(birthdate) = 2023 AND MONTH(birthdate) = 01 AND DAY(birthdate) = 10);