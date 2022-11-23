-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "vineyards" (
    "place_id" VARCHAR   NOT NULL,
    "name" VARCHAR,   NOT NULL,
    "business_status" VARCHAR(50),   NOT NULL,
    "formatted_phone_number" VARCHAR(50),   NOT NULL,
    "formatted_address" VARCHAR,   NOT NULL,
    "url" VARCHAR,   NOT NULL,
    "website" VARCHAR,   NOT NULL,
    "rating" REAL,   NOT NULL,
    "user_ratings_total" INTEGER,   NOT NULL,
    "street_address" VARCHAR,   NOT NULL,
    "city" VARCHAR(50),   NOT NULL,
    "province" VARCHAR(50),   NOT NULL,
    "zipcode" VARCHAR(50),   NOT NULL,
    "country" VARCHAR(50),   NOT NULL,
    "location_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_vineyards" PRIMARY KEY (
        "place_id"
     )
);

CREATE TABLE "vineyard_reviews" (
    "author_name" VARCHAR,   NOT NULL,
    "author_url" VARCHAR,   NOT NULL,
    "original_language" VARCHAR(50),   NOT NULL,
    "rating" SMALLINT,   NOT NULL,
    "relative_time_description" VARCHAR(50),   NOT NULL,
    "text" VARCHAR,   NOT NULL,
    "time" BIGINT,   NOT NULL,
    "translated" BOOLEAN,   NOT NULL,
    "place_id" VARCHAR,   NOT NULL,
    "review_id" BIGINT   NOT NULL,
    CONSTRAINT "pk_vineyard_reviews" PRIMARY KEY (
        "review_id"
     )
);

CREATE TABLE "geometry" (
    "center_lat" REAL,   NOT NULL,
    "center_lon" REAL,   NOT NULL,
    "northeast_lat" REAL,   NOT NULL,
    "northeast_lon" REAL,   NOT NULL,
    "southwest_lat" REAL,   NOT NULL,
    "southwest_lon" REAL,   NOT NULL,
    "place_id" VARCHAR   NOT NULL,
    CONSTRAINT "pk_geometry" PRIMARY KEY (
        "place_id"
     )
);

CREATE TABLE "photos" (
    "photo_id" INTEGER   NOT NULL,
    "photo_reference" VARCHAR,   NOT NULL,
    "place_id" VARCHAR,   NOT NULL,
    "height" INTEGER,   NOT NULL,
    "width" INTEGER,   NOT NULL,
    "uploader_url" VARCHAR,   NOT NULL,
    "uploader_name" VARCHAR(50)   NOT NULL,
    CONSTRAINT "pk_photos" PRIMARY KEY (
        "photo_id"
     )
);

ALTER TABLE "vineyard_reviews" ADD CONSTRAINT "fk_vineyard_reviews_place_id" FOREIGN KEY("place_id")
REFERENCES "vineyards" ("place_id");

ALTER TABLE "geometry" ADD CONSTRAINT "fk_geometry_place_id" FOREIGN KEY("place_id")
REFERENCES "vineyards" ("place_id");

ALTER TABLE "photos" ADD CONSTRAINT "fk_photos_place_id" FOREIGN KEY("place_id")
REFERENCES "vineyards" ("place_id");

