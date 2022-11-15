-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE 'brand' ('brand_id' SERIAL PRIMARY KEY, 'brand_name' VARCHAR(50))

CREATE TABLE "vineyards" (
    "place_id" VARCHAR PRIMARY KEY,
    "name" VARCHAR  NOT NULL,
    "business_status" VARCHAR(50),
    "formatted_phone_number" VARCHAR(50),
    "formatted_address" VARCHAR,
    "url" VARCHAR,
    "website" VARCHAR,
    "rating" REAL,
    "total_ratings" INTEGER,
    "street_address" VARCHAR,
    "city" VARCHAR(50),
    "province" VARCHAR(50),
    "zipcode" VARCHAR(50),
    "country" VARCHAR(50),
    "location_name" VARCHAR,
    "center_lat" REAL,
    "center_lon" REAL,
    "northeast_lat" REAL, 
    "northeast_lon" REAL, 
    "southwest_lat" REAL, 
    "southwest_lon" REAL, 
    "brand_id" INTEGER REFERENCES brand(brand_id)
     )
);

CREATE TABLE "vineyard_reviews" (
    "author_name" VARCHAR,
    "author_url" VARCHAR,
    "original_language" VARCHAR(50),
    "rating" SMALLINT,   
    "relative_time_description" VARCHAR(50),   
    "text" VARCHAR,
    "time" BIGINT, 
    "translated" BOOLEAN,
    "place_id" VARCHAR REFERENCES vineyards(place_id)
    "review_id" BIGINT PRIMARY KEY,
);

CREATE TABLE 'wine_reviews' (
    'winery' VARCHAR,
    'vintage' INTEGER, 
    'variety' VARCHAR,
    'designation' VARCHAAR,
    'score' INTEGER,
    'category' VARCHAR,
    'title' VARCHAR,
    'ava' VARCHAR,
    'region' VARCHAR,
    'province' VARCHAR,
    'country' VARCHAR,
    'release_price'VARCHAR,
    'source' VARCHAR,
    'brand_id' INTEGER REFERENCES brand(brand_id)
    );
