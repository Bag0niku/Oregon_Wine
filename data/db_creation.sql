-- logged in as superuser -- 

CREATE DATABASE vineyard_wine;

DROP DATABASE postgres;

REVOKE ALL ON SCHEMA public FROM public;

REVOKE ALL ON DATABASE postgres FROM public;

CREATE USER web;

CREATE TABLE vineyards (
             place_id VARCHAR PRIMARY KEY, 
             business_name VARCHAR NOT NULL,
             location_name VARCHAR,   
             phone VARCHAR,
             rating REAL,
             user_ratings_total INTEGER,
             formatted_address VARCHAR NOT NULL,
             street_address VARCHAR(100),
             city VARCHAR(50) NOT NULL,
             province VARCHAR(50) NOT NULL,
             zipcode VARCHAR NOT NULL,
             country_code VARCHAR(50) NOT NULL,
             region VARCHAR(50),
             subregion VARCHAR(50),
             status VARCHAR(50) NOT NULL,
             gmaps_url VARCHAR
);

CREATE TABLE reviews (review_id BIGSERIAL PRIMARY KEY,
             place_id VARCHAR REFERENCES vineyards(place_id) ON DELETE CASCADE,
             author_name VARCHAR(50), 
             author_url VARCHAR,
             original_language VARCHAR(50), 
             translated BOOLEAN,
             utc_time BIGINT,
	         relative_time_description VARCHAR(50),
             rating INTEGER,
             review_text VARCHAR
);

CREATE TABLE geometry (
             place_id varchar REFERENCES vineyards(place_id) ON DELETE CASCADE,
             center_lat REAL,
             center_lon REAL, 
             northeast_lat REAL, 
             northeast_lon REAL, 
             southwest_lat REAL, 
             southwest_lon REAL,
             PRIMARY KEY (place_id)
  );

CREATE TABLE photos (
             photo_id BIGSERIAL PRIMARY KEY,
             height INTEGER,
             width INTEGER,
             photo_reference VARCHAR,
             place_id VARCHAR REFERENCES vineyards(place_id) ON DELETE CASCADE,
             uploader_url VARCHAR,
             uploader_name VARCHAR(50)
  );
    
  
GRANT CONNECT ON DATABASE vineyard_wine TO web;

GRANT SELECT ON vineyards, reviews, photos, geometry TO web;
  
