SELECT name FROM  people
WHERE id IN
(SELECT DISTINCT(person_id) FROM
movies JOIN stars
ON id = movie_id
WHERE year = 2004) ORDER BY birth;