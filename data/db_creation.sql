

CREATE TABLE "brand" (
    "brand_name" VARCHAR PRIMARY KEY,
    "grapes" JSON,
    "style" VARCHAR ,
    "rating" INTEGER
);

CREATE TABLE "regions" (
    "region_id" SERIAL PRIMARY KEY,
    "region_name" VARCHAR(50)   NOT NULL,
    "subregion" BOOLEAN   NOT NULL,
    "gps_border" JSON 
);

CREATE TABLE "vineyards" (
    "place_id" VARCHAR   PRIMARY KEY,
    "business_name" VARCHAR NOT NULL,
    "location_name" VARCHAR,
    "phone" VARCHAR ,
    "rating" REAL ,
    "user_ratings_total" INTEGER   NOT NULL,
    "formatted_address" VARCHAR   NOT NULL,
    "street_address" VARCHAR(100),
    "city" VARCHAR(50)   NOT NULL,
    "province" VARCHAR(50)   NOT NULL,
    "zipcode" VARCHAR,
    "country_code" VARCHAR(50)   NOT NULL,
    "region" INTEGER  REFERENCES regions(region_id),
    "subregion" INTEGER REFERENCES regions(region_id),
    "status" VARCHAR(50),
    "gmaps_url" VARCHAR ,
    "brand_name" VARCHAR REFERENCES brand(brand_name) NOT NULL
);

CREATE TABLE "vineyard_reviews" (
    "place_id" VARCHAR  REFERENCES vineyards(place_id) NOT NULL,
    "brand_name" VARCHAR  REFERENCES brand(brand_name) NOT NULL,
    "author_name" VARCHAR(50)   NOT NULL,
    "author_url" VARCHAR,
    "original_language" VARCHAR(50)   NOT NULL,
    "translated" BOOLEAN   NOT NULL,
    "utc_time" BIGINT   NOT NULL,
    "relative_time_description" VARCHAR(50),
    "rating" INTEGER   NOT NULL,
    "review_text" VARCHAR,
    "review_source" VARCHAR  NOT NULL,
    CONSTRAINT "pk_vineyard_reviews" PRIMARY KEY (
        "place_id","author_name","utc_time"
     )
);

CREATE TABLE "geometry" (
    "place_id" varchar   PRIMARY KEY REFERENCES "vineyards" ("place_id"),
    "center_lat" REAL   NOT NULL,
    "center_lon" REAL   NOT NULL,
    "northeast_lat" REAL   NOT NULL,
    "northeast_lon" REAL   NOT NULL,
    "southwest_lat" REAL   NOT NULL,
    "southwest_lon" REAL   NOT NULL
);

CREATE TABLE "photos" (
    "photo_id" BIGSERIAL  PRIMARY KEY,
    "height" INTEGER   NOT NULL,
    "width" INTEGER   NOT NULL,
    "photo_reference" VARCHAR   NOT NULL,
    "place_id" VARCHAR REFERENCES "vineyards" ("place_id")  NOT NULL,
    "uploader_url" VARCHAR   NOT NULL,
    "uploader_name" VARCHAR(50)   NOT NULL
);

CREATE TABLE "wine_reviews" (
    "wine_id" VARCHAR REFERENCES wine(wine_id)  NOT NULL,
    "brand_name" VARCHAR REFERENCES brand(brand_name)  NOT NULL,
    "author_name" VARCHAR(50)   NOT NULL,
    "author_url" VARCHAR   NOT NULL,
    "original_language" VARCHAR(50)   NOT NULL,
    "translated" BOOLEAN   NOT NULL,
    "utc_time" BIGINT   NOT NULL,
    "relative_time_description" VARCHAR(50)   NOT NULL,
    "rating" INTEGER   NOT NULL,
    "review_text" VARCHAR,
    "review_source" VARCHAR   NOT NULL,
    CONSTRAINT "pk_wine_reviews" PRIMARY KEY (
        "wine_id","author_name","utc_time"
     )
);

CREATE TABLE "wine" (
    "wine_id" BIGSERIAL  PRIMARY KEY,
    "brand_name" VARCHAR   REFERENCES brand(brand_name) NOT NULL,
    "vinetage" INTEGER   NOT NULL,
    "type" VARCHAR ,
    "style" VARCHAR ,
    "grapes" JSON ,
    "region" VARCHAR  REFERENCES regions(region_id),
    "subregion" VARCHAR  REFERENCES regions(region_id),
    "country" VARCHAR   NOT NULL
);

CREATE TABLE "grapes" (
    "varietal_id" SERIAL   NOT NULL,
    "varietal_name" VARCHAR(50)   NOT NULL,
    CONSTRAINT "pk_grapes" PRIMARY KEY (
        "varietal_id"
     )
);
