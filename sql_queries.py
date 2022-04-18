# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
  (
     songplay_id SERIAL PRIMARY KEY,
     start_time  TIMESTAMP NOT NULL,
     user_id     INT NOT NULL,
     level       VARCHAR,
     song_id     VARCHAR,
     artist_id   VARCHAR,
     session_id  INT,
     location    VARCHAR,
     useragent   VARCHAR
  ) 
  """)

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
  (
     user_id    INT PRIMARY KEY,
     first_name VARCHAR,
     last_name  VARCHAR,
     gender     VARCHAR,
     level      VARCHAR
  ) 
  """)

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
  (
     song_id   VARCHAR PRIMARY KEY,
     title     VARCHAR NOT NULL,
     artist_id VARCHAR,
     year      INT,
     duration  NUMERIC NOT NULL
  ) 
  """)

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists 
(   
    artist_id varchar PRIMARY KEY,
    name varchar NOT NULL, 
    location varchar, 
    latitude DOUBLE PRECISION, 
    longitude DOUBLE PRECISION
)
  """)

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
  (
     start_time TIMESTAMP PRIMARY KEY,
     hour       INT,
     day        INT,
     month      INT,
     year       INT,
     weekday    INT
  ) """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays
            (
                        start_time,
                        user_id,
                        level,
                        song_id,
                        artist_id,
                        session_id,
                        location,
                        useragent
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        songplay_id
            )
            do nothing
""")

user_table_insert = ("""INSERT INTO users
            (
                        user_id,
                        first_name,
                        last_name,
                        gender,
                        level
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        user_id
            )
            do update set level = excluded.level || users.level
""")

song_table_insert = ("""INSERT INTO songs
            (
                        song_id,
                        title,
                        artist_id,
                        year,
                        duration
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        song_id
            )
            do nothing
""")

artist_table_insert = ("""INSERT INTO artists
            (
                        artist_id,
                        NAME,
                        location,
                        latitude,
                        longitude
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        artist_id
            )
            do nothing
""")


time_table_insert = ("""INSERT INTO time
            (
                        start_time,
                        hour,
                        day,
                        month,
                        year,
                        weekday
            )
            VALUES
            (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
            )
ON conflict
            (
                        start_time
            )
            do nothing
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id,
       a.artist_id
FROM   songs s
       join artists a
         ON s.artist_id = a.artist_id
WHERE  s.title = 'I Didn''t Mean To'
       AND a.name = 'Casual'
       AND s.duration = 218.93179; """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]