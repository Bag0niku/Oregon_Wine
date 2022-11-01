-- logged in as superuser -- 

CREATE DATABASE vineyard_wine;

DROP DATABASE postgres;

REVOKE ALL ON SCHEMA public FROM public;

REVOKE ALL ON DATABASE postgres FROM public;

CREATE USER web;

CREATE TABLE vineyards (
             place_id VARCHAR PRIMARY KEY, 
             business_name VARCHAR,
             location_name VARCHAR,   
             phone VARCHAR,
             rating REAL,
             user_ratings_total INTEGER,
             formatted_address VARCHAR,
             street_address_1 VARCHAR(100),
             street_address_2 VARCHAR(100),
             locality VARCHAR(50),
             city VARCHAR(50),
             province VARCHAR(50),
             zipcode VARCHAR,
             country VARCHAR(50),
             region VARCHAR(50),
             subregion VARCHAR(50),
             status VARCHAR(50),
             gmaps_url VARCHAR,
);

CREATE TABLE reviews (
             place_id VARCHAR REFERENCES vineyards(place_id) ON DELETE CASCADE,
             author_name VARCHAR(50), 
             author_url VARCHAR,
             original_language VARCHAR(50), 
             translated BOOLEAN,
             utc_time TIMESTAMP,
             relative_time_description VARCHAR(50),
             rating INTEGER,
             review_text VARCHAR
);

CREATE TABLE geometry (
             place_id REFERENCES vineyards(place_id) ON DELETE CASCADE,
             center_lat REAL,
             center_lon REAL, 
             northeast_lat REAL, 
             northeast_lon REAL, 
             southwest_lat REAL, 
             southwest_lon REAL,
             PRIMARY KEY (place_id)
  );

CREATE TABLE photos (
             photo_id INTEGER GENERATED ALWAYS AS IDENTITY,
             height INTEGER,
             width INTEGER,
             photo_reference VARCHAR,
             place_id VARCHAR REFERENCES vineyards(place_id) ON DELETE CASCADE,
             uploader_link VARCHAR,
             uploader_name VARCHAR(50),
             PRIMARY KEY (photo_id)  
  );
  
  
GRANT CONNECT ON DATABASE vineyard_wine TO web;

GRANT SELECT ON vineyards, reviews, photos, geometry TO web;
  
