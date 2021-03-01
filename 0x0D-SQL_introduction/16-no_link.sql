-- Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- Dont list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name is not NULL
ORDER BY score DESC;
