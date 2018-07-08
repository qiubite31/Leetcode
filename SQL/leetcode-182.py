"""
182. Duplicate Emails
Difficulty: Easy
Related Topic: SQL

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.
"""
# Write your MySQL query statement below
SELECT EMAIL
  FROM (SELECT EMAIL, COUNT(EMAIL) CNT FROM PERSON
         GROUP BY EMAIL      
       ) P
 WHERE CNT >= 2