-- Import the database dump from hbtn_0d_tvshows to your MySQL server.
-- Lscript that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- The column must first be 'genre' and second be 'number_of_shows.
-- Don’t display a genre that doesn’t have any shows linked.
-- Results must be sorted in descending order by the number of shows linked.
-- The database name will be passed as an argument of the mysql command.

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
	FROM tv_genres
	JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
