# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id int PRIMARY KEY, 
                            start_time int, user_id varchar, level varchar, 
                            song_id varchar NOT NULL, artist_id varchar NOT NULL, session_id int NOT NULL,
                            location varchar, userAgent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar PRIMARY KEY, first_name varchar, last_name varchar, gender varchar,level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration int)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar, location varchar, latitude int, longitude int)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time int, hour int, day int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, 
                            song_id, artist_id, session_id, location, userAgent) 
                            VALUES ()
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender,level)
                         VALUES ()
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                        VALUES (%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)
                          VALUES ()
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, month, year, weekday)
                        VALUES ()
""")

# FIND SONGS

song_select = ("""SELECT * FROM song_table WHERE song_id = "SOCIWDW12A8C13D406"
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]