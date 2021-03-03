-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT a.name FROM tv_genres a
JOIN tv_show_genres b ON a.id = b.genre_id
JOIN tv_shows c ON b.show_id = c.id WHERE c.title = "Dexter"
ORDER BY a.name ASC;
