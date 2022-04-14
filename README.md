## Data Modelling with PostgreSQL 
--------

### Project Summary

This project builds a data model using postgresql. In the model a music database called sparkifydb which demonstrates a STAR schema is developed and ingested with data from two datasets, song_data and log_data. ETL is performed on both files to process and collect the required data. Prior to this, SQL queries were written to create the needed tables and insert into the table. The ETL was first performed in jupyter notebook etl.ipynb to develop the tables before completing and loading whole dataset in etl.py. The five tables created for the sparkifydb includes 

* Songs Table
---
   This table records details of the songs such as the title, songId, artistId, year and duration. 
* Artists Table
---
   In this table, the records of artists are stored. Artists records such as name, location, longitude and latitude are included in the table
* Times Table
---
   This table comprises the timestamp (ts) in the log_file data. The records are converted to datetime and used to create records such as hour, day, month,and year for the table. 
* Users Table
---
   The users records such as first name, last name, gender, and level are recorded in this table. 
* Songplays Table
---
   Consists of records with page "NextSong". 

### How to run the Scripts
