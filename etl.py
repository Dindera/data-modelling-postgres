import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Reads the song_data file.

    Processes the song_data.

    Inserts data into song and artists tables.

    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = {"song_id": df.song_id, "title": df.title, "artist_id": df.artist_id, "year": df.year, "duration": df.duration}
    song_data = pd.DataFrame(song_data)
    song_data = song_data.values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = artist_data = {"artist_id": df.artist_id, "name": df.artist_name, "location": df.artist_location, "latitude": df.artist_latitude, "longitude": df.artist_longitude}
    artist_data = pd.DataFrame(artist_data)
    artist_data = artist_data.values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Reads the log_data file.

    Processes the log_data.

    Transforms the timestamp data and inserts into the time table.

    Inserts into the users table.

    Selects from songs and artist table based on title, name and duration.

    Inserts into songplays table based on song title, artist name and song duration.
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=="NextSong"]
    
    # convert timestamp column to datetime
    df['timestamp'] = pd.to_datetime(df['ts'])
    t = pd.DataFrame(df['timestamp'])
    
    # insert time data records
    time_data = {"start_time": t['timestamp'], "hour": t['timestamp'].dt.hour, "day": t['timestamp'].dt.day, "month":t['timestamp'].dt.month, "year": t['timestamp'].dt.year, "weekday": t['timestamp'].dt.weekday}
    time_df = time_df = pd.DataFrame(data=time_data)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = {'user_id': df['userId'], 'first_name': df['firstName'], 'last_name': df['lastName'], 'gender': df['gender'], 'level': df['level']}
    user_df = pd.DataFrame(user_df)

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.timestamp, row.userId, row.level, songid,artistid,row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Gets and appends data from same dir to a list.

    Counts files found and processed in a dir.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Establishes connection to the database sparkifydb and gets cursor in it.

    Processes data in song_data and log_data filepath.

    Inserts into all tables - songs, artist, time, users and songplay.

    Connection close.
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()